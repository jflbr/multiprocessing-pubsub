from .logger import get_logger


class Logger:
    def on_motion_vector(self, motion_vector: bytes):
        logger = get_logger("DeviceLogger")
        logger.debug(f"Received: {motion_vector!r}")

    def on_detection_vector(self, detection_vector):
        logger = get_logger("DeviceLogger")
        logger.debug(f"Received: {detection_vector!r}")
