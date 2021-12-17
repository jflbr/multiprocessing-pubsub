import logging

from faker import Faker

from motion_detection.protocols.messages import (
    BoundingBox,
    DetectionVector,
    MotionVector,
    VelocityVector,
)

logging.getLogger("faker.factory").setLevel(logging.ERROR)


faker = Faker(["en_US", "fr_FR"])


def fake_detection_vector() -> DetectionVector:
    return DetectionVector(
        timestamp=faker.date_time_this_month(),
        frame_id=faker.random_int(),
        classification="42% python",
        bounding_box=BoundingBox(1, 1, 1, 1),
    )


def fake_motion_vector() -> MotionVector:
    return MotionVector(
        timestamp=faker.date_time_this_month(),
        frame_id=faker.random_int(),
        classification="42% python",
        bounding_box=BoundingBox(1, 1, 1, 1),
        velocity_vector=VelocityVector(1.0, 1),
    )
