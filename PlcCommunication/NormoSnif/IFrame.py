from enum import IntEnum
from typing import Protocol


class IFrame(Protocol):
    class MemAreaDesignation(IntEnum):
        ...
