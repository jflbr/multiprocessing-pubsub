from motion_detection.device_logger import Logger
from motion_detection.devices import MotionDetector, SingleShotDetector
from motion_detection.logger import get_logger
from motion_detection.protocols.multiprocessing_pubsub import (
    PublishWorker,
    SubscriptionWorker,
    TopicRegistry,
)

LOGGER = get_logger()


if __name__ == "__main__":
    registry = TopicRegistry()
    motion_vector = registry.topic_queue("MotionVector")
    detection_vector = registry.topic_queue("DetectionVector")

    # application entities
    motion_detector = MotionDetector()  # publisher=motion_vector)
    singleshot_detector = SingleShotDetector(
        publisher=detection_vector
    )  # pubsub
    device_logger = Logger()

    # workers for application entities
    subscription_worker = SubscriptionWorker(motion_vector)
    publishing_worker = PublishWorker(
        motion_vector, motion_detector.start_detection
    )
    detection_vector_subscription_worker = SubscriptionWorker(
        detection_vector
    )

    subscription_worker.register_callback(singleshot_detector.onMotionVector)
    subscription_worker.register_callback(device_logger.on_motion_vector)
    detection_vector_subscription_worker.register_callback(
        device_logger.on_motion_vector
    )

    workers = [
        subscription_worker,
        publishing_worker,
        detection_vector_subscription_worker,
    ]
    for worker in workers:
        worker.start()

    try:
        for worker in workers:
            worker.join()
    except KeyboardInterrupt:
        for worker in workers:
            worker.terminate()
    finally:
        motion_vector.close()
        motion_vector.join_thread()
        detection_vector.close()
        detection_vector.join_thread()

    LOGGER.info("Gnuk gnuk.")
