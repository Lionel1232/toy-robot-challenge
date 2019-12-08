from enum import Enum


class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


class Turn(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


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


class Position:
    def __init__(self, x: int, y: int, orientation: Orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def __repr__(self) -> str:
        return f"{self.x},{self.y},{self.orientation.direction.value}"
