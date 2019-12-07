from enum import Enum


class Position:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def __repr__(self):
        return f"{self.x},{self.y},{self.orientation.direction.value}"


class Orientation:
    def __init__(self, direction, left_direction, right_direction):
        self.direction = direction
        self._left = left_direction
        self._right = right_direction

    def get_direction(self, turn):
        if turn == Turn.LEFT:
            return self._left
        if turn == Turn.RIGHT:
            return self._right


class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


class Turn(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
