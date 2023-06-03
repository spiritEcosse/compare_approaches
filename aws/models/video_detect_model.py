from _decimal import Decimal
from dataclasses import dataclass
from typing import List, Dict

from mashumaro.config import BaseConfig
from mashumaro.types import SerializationStrategy
from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class BoundingBox(DataClassJSONMixin):
    Height: float
    Left: float
    Top: float
    Width: float


class FormattedPoint(SerializationStrategy):
    def __init__(self, precision):
        self.precision = precision

    def deserialize(self, value: str) -> Decimal:
        return Decimal(value).quantize(Decimal(self.precision))

    def serialize(self, value: Decimal) -> str:
        return str(value)


@dataclass
class Polygon(DataClassJSONMixin):
    X: float
    Y: float

    class Config(BaseConfig):
        serialization_strategy = {
            float: FormattedPoint(".0")
        }


@dataclass
class Geometry(DataClassJSONMixin):
    BoundingBox: BoundingBox
    Polygon: List[Polygon]


@dataclass
class TextDetection(DataClassJSONMixin):
    Confidence: float
    DetectedText: str
    Geometry: Geometry
    Id: int
    Type: str


@dataclass
class ResponseMetadata(DataClassJSONMixin):
    HTTPHeaders: Dict[str, str]
    HTTPStatusCode: int
    RequestId: str
    RetryAttempts: int


@dataclass
class VideoMetadata(DataClassJSONMixin):
    Codec: str
    ColorRange: str
    DurationMillis: int
    Format: str
    FrameHeight: int
    FrameRate: float
    FrameWidth: int


@dataclass
class TextDetections(DataClassJSONMixin):
    TextDetection: TextDetection
    Timestamp: int

    def commercial_text(self):
        return self.TextDetection.Type == 'WORD'


@dataclass
class VideoDetectModel(DataClassJSONMixin):
    JobStatus: str
    NextToken: str
    ResponseMetadata: ResponseMetadata
    TextDetections: List[TextDetections]
    TextModelVersion: str
    VideoMetadata: VideoMetadata
