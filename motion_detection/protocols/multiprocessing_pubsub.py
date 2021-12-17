import multiprocessing
from typing import Dict

from motion_detection.protocols.pubsub import ReadWriteQueue


class SubscriptionWorker(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self._queue = queue
        self.callbacks = []

    def register_callback(self, cb):
        if cb not in self.callbacks:
            self.callbacks.append(cb)

    def run(self):
        while True:
            message = self._queue.get()
            for callback in self.callbacks:
                callback(message)


class PublishWorker(multiprocessing.Process):
    def __init__(self, topic, publishing_task):
        super().__init__()
        self._topic = topic
        self._publishing_task = publishing_task

    def run(self):
        self._publishing_task(self._topic)


class TopicRegistry:
    def __init__(self) -> None:
        self._queues: Dict[str, ReadWriteQueue] = {}

    def topic_queue(self, topic):
        if topic not in self._queues:
            self._queues[topic] = multiprocessing.Queue()
        return self._queues[topic]
