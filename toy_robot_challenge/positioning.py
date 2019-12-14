from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Turn(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def dx(self) -> int:
        return 1 if self is Direction.EAST else -1 if self is Direction.WEST else 0

    @property
    def dy(self) -> int:
        return 1 if self is Direction.NORTH else -1 if self is Direction.SOUTH else 0

    @property
    def left(self) -> Direction:
        new_direction = (self.value - 1) % 4
        return Direction(new_direction)

    @property
    def right(self) -> Direction:
        new_direction = (self.value + 1) % 4
        return Direction(new_direction)


@dataclass
class Position:
    x: int
    y: int
    direction: Direction

    def __str__(self) -> str:
        return f"{self.x},{self.y},{self.direction.name}"
