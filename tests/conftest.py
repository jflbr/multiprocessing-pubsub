import pytest

from tests.protocols.fake_messages import (
    fake_detection_vector,
    fake_motion_vector,
)


class ReadWriteQueue:
    def __init__(self) -> None:
        self.last_message = None
        self.message_to_get = None

    def put(self, message):
        self.last_message = message

    def get(self):
        return self.message_to_get


class MessageHandler:
    def __init__(self) -> None:
        self.last_message = None

    def __call__(self, message):
        # fake_bytes_message = b"{}"
        # publisher.put(fake_bytes_message)
        self.last_message = message


class PublishingTask:
    def __init__(self) -> None:
        self.last_message = None

    def __call__(self, queue):
        fake_bytes_message = b"{}"
        queue.put(fake_bytes_message)
        self.last_message = fake_bytes_message


@pytest.fixture
def fake_read_write_queue():
    return ReadWriteQueue()


@pytest.fixture
def fake_message_handler():
    return MessageHandler()


@pytest.fixture
def fake_publishing_task():
    return PublishingTask()


@pytest.fixture
def detection_vector():
    return fake_detection_vector()


@pytest.fixture
def motion_vector():
    return fake_motion_vector()
