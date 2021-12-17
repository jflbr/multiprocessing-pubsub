import pytest

from motion_detection.protocols.multiprocessing_pubsub import (
    SubscriptionWorker,
)


def test_unique_registration_per_callback(
    fake_read_write_queue, fake_message_handler
):
    susbscription_worker = SubscriptionWorker(fake_read_write_queue)
    assert not susbscription_worker.callbacks
    for _ in range(2):
        susbscription_worker.register_callback(fake_message_handler)

    assert len(susbscription_worker.callbacks) == 1
    assert susbscription_worker.callbacks[0] == fake_message_handler


@pytest.mark.skip(
    reason=(
        "Find a workaound to bypass the infinite loop. Test with a"
        " 'killable thread' or use a control queue."
    )
)
def test_callbacks_are_called_on_new_messages(
    fake_read_write_queue, fake_message_handler
):
    susbscription_worker = SubscriptionWorker(fake_read_write_queue)
    susbscription_worker.register_callback(fake_message_handler)
    assert fake_message_handler.last_message is None
    fake_read_write_queue.message_to_get = b"Gotcha"

    # TODO: wrap run(...) call with a 'killable thread'
    susbscription_worker.run()

    assert isinstance(fake_message_handler.last_message, bytes)
    fake_message_handler.last_message == b"Gotcha"
