import json
import time

import pydantic

from motion_detection.protocols.messages import DetectionVector, MotionVector
from motion_detection.protocols.pubsub import ReadWriteQueue

from .logger import get_logger


class MotionDetector:
    # def __init__(self, publisher) -> None:
    #     self.publisher = publisher

    def start_detection(self, publisher: ReadWriteQueue):
        logger = get_logger("MotionDetector")
        from tests.protocols.fake_messages import fake_motion_vector

        # TODO: Consider controlling the execution using an additional queue
        while True:
            motion_vector: MotionVector = fake_motion_vector()
            logger.debug(
                "Publishing MotionVector with frame ID "
                f"{motion_vector.frame_id}..."
            )
            publisher.put(motion_vector.json().encode("utf-8"))
            time.sleep(0.5)


class SingleShotDetector:
    def __init__(self, publisher: ReadWriteQueue) -> None:
        self.publisher = publisher

    def onMotionVector(self, motion_vector_payload: bytes):
        logger = get_logger("SingleShotDetector")
        try:
            motion_vector = MotionVector(**json.loads(motion_vector_payload))
        except (pydantic.ValidationError, TypeError) as err:
            logger.error(
                f"Received invalid motion vector \n\t"
                f"{motion_vector_payload!r}"
            )
            logger.error(f"\t{err}")
            raise

        logger.debug(
            f"Received MotionVector with frame ID {motion_vector.frame_id}"
        )

        from tests.protocols.fake_messages import fake_detection_vector

        detection_vector: DetectionVector = fake_detection_vector()
        logger.debug(
            "Publishing DetectionVector with frame ID "
            f"{detection_vector.frame_id}..."
        )
        self.publisher.put(detection_vector.json().encode("utf-8"))
        time.sleep(0.2)
