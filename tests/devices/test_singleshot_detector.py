import pydantic
import pytest

from motion_detection.devices import SingleShotDetector
from tests.conftest import ReadWriteQueue


def test_invalid_message_type(fake_read_write_queue: ReadWriteQueue):
    singleshot_detector = SingleShotDetector(fake_read_write_queue)
    for message_with_invalid_type in {42, False}:
        with pytest.raises(TypeError):
            singleshot_detector.onMotionVector(message_with_invalid_type)  # type: ignore


def test_malformed_message(fake_read_write_queue: ReadWriteQueue):
    singleshot_detector = SingleShotDetector(fake_read_write_queue)
    message_with_invalid_type = b'{"foo": 42, "bar": false}'
    with pytest.raises(pydantic.ValidationError):
        singleshot_detector.onMotionVector(message_with_invalid_type)


def test_put_message_type(
    fake_read_write_queue: ReadWriteQueue, motion_vector
):
    singleshot_detector = SingleShotDetector(fake_read_write_queue)
    assert fake_read_write_queue.last_message is None
    singleshot_detector.onMotionVector(motion_vector.json().encode("utf-8"))
    assert isinstance(fake_read_write_queue.last_message, bytes)
