from typing import Protocol


class ReadWriteQueue(Protocol):
    def put(self, message: bytes):
        ...

    def get(self) -> bytes:
        ...
