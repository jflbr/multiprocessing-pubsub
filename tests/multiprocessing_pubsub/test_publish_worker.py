from motion_detection.protocols.multiprocessing_pubsub import PublishWorker

# from motion_detection.protocols.pubsub import ReadWriteQueue


def test_worker_target_is_properly_called(
    fake_read_write_queue, fake_publishing_task
):
    pub_worker = PublishWorker(fake_read_write_queue, fake_publishing_task)
    assert fake_publishing_task.last_message is None
    assert fake_read_write_queue.last_message is None

    pub_worker.run()

    assert isinstance(fake_publishing_task.last_message, bytes)
    assert (
        fake_read_write_queue.last_message
        == fake_publishing_task.last_message
    )
