from dataclasses import dataclass
from enum import Enum


class Turn(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Direction(Enum):
    NORTH = {Turn.LEFT: "WEST", Turn.RIGHT: "EAST"}
    SOUTH = {Turn.LEFT: "EAST", Turn.RIGHT: "WEST"}
    EAST = {Turn.LEFT: "NORTH", Turn.RIGHT: "SOUTH"}
    WEST = {Turn.LEFT: "SOUTH", Turn.RIGHT: "NORTH"}

    @property
    def dx(self):
        return 1 if self is Direction.EAST else -1 if self is Direction.WEST else 0

    @property
    def dy(self):
        return 1 if self is Direction.NORTH else -1 if self is Direction.SOUTH else 0


class Orientation:
    def __init__(
        self,
        direction: Direction,
        left_direction: Direction,
        right_direction: Direction,
    ):
        self.direction = direction
        self._left = left_direction
        self._right = right_direction

    def get_direction(self, turn: Turn) -> Direction:
        if turn == Turn.LEFT:
            return self._left
        else:
            return self._right


@dataclass
class Position:
    x: int
    y: int
    direction: Direction

    def __str__(self) -> str:
        return f"{self.x},{self.y},{self.direction.name}"
