import dataclasses
from datetime import datetime

import pydantic


@dataclasses.dataclass
class BoundingBox:
    x: float = 0
    y: float = 0
    width: float = 0
    height: float = 0


@dataclasses.dataclass
class VelocityVector:
    speed: float = 0
    direction: float = 0


class DetectionVector(pydantic.BaseModel):
    timestamp: datetime = pydantic.Field(
        default=...,
        description="Vector creation date",
    )
    frame_id: int = pydantic.Field(
        default=...,
        description="Vector frame ID",
        example=42,
    )
    classification: str = pydantic.Field(
        default=...,
        description="Prediction vector",
        examples=[
            "car 98%",
            "bike 5%",
        ],
    )
    bounding_box: BoundingBox = pydantic.Field(
        default=...,
        description=(
            "Bounding box (x, y, width, height) of a part "
            "of the image where motion is detected"
        ),
        example=BoundingBox(0, 0, 0, 0),
    )


class MotionVector(pydantic.BaseModel):
    timestamp: datetime = pydantic.Field(
        default=...,
        description="Vector creation date",
    )
    frame_id: int = pydantic.Field(
        default=...,
        description="Vector frame ID",
        example=42,
    )
    bounding_box: BoundingBox = pydantic.Field(
        default=...,
        description=(
            "Bounding box (x, y, width, height) of a part "
            "of the image where motion is detected"
        ),
        example=BoundingBox(0, 0, 0, 0),
    )
    velocity_vector: VelocityVector = pydantic.Field(
        default=...,
        description="Velocity vector (2d vector, with speed and direction)",
        example=VelocityVector(1.0, 1),
    )

    class Config:
        json_encoders = {datetime: lambda dt: dt.timestamp()}
