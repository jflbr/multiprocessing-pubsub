from motion_detection.protocols.multiprocessing_pubsub import TopicRegistry


def test_unique_queue_per_topic_name():
    registry = TopicRegistry()
    topic_name = "fizz"
    initial_queue = registry.topic_queue(topic_name)
    for _ in range(2):
        next_queue = registry.topic_queue(topic_name)
        assert initial_queue == next_queue
    assert len(registry._queues) == 1
