import pytest

from motion_detection.devices import MotionDetector
from tests.conftest import ReadWriteQueue


@pytest.mark.skip(
    reason=(
        "Find a workaound to bypass the infinite loop. Test with a"
        " 'killable thread' or use a control queue."
    )
)
def test_put_message_type(fake_read_write_queue: ReadWriteQueue):
    _ = MotionDetector()
    assert fake_read_write_queue.last_message is None
    # TODO: wrap start_detection(...) call into a 'killable thread'
