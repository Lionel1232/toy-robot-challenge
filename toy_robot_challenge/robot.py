import copy
import logging
from typing import Dict, Optional

from .positioning import Direction, Orientation, Position, Turn
from .table import Table

logger = logging.getLogger(__name__)


class Robot:
    def __init__(self, table: Table):
        self._position: Optional[Position] = None
        self._table = table
        self._orientations: Dict[Direction, Orientation] = {
            Direction.NORTH: Orientation(
                Direction.NORTH, Direction.WEST, Direction.EAST
            ),
            Direction.EAST: Orientation(
                Direction.EAST, Direction.NORTH, Direction.SOUTH
            ),
            Direction.SOUTH: Orientation(
                Direction.SOUTH, Direction.EAST, Direction.WEST
            ),
            Direction.WEST: Orientation(
                Direction.WEST, Direction.SOUTH, Direction.NORTH
            ),
        }

    def place(self, x: int, y: int, direction: Direction) -> None:
        placement = Position(x, y, self._orientations[direction])
        if self._table.valid_position(placement):
            self._position = placement

    def report(self) -> None:
        if self._is_placed():
            logger.info(self._position)

    def rotate(self, turning_direction: Turn) -> None:
        if not self._is_placed():
            return

        self._position.orientation = self._orientations[
            self._position.orientation.get_direction(turning_direction)
        ]

    def move(self) -> None:
        if not self._is_placed():
            return

        new_position = copy.copy(self._position)
        if self._position.orientation.direction is Direction.NORTH:
            new_position.y += 1

        if self._position.orientation.direction is Direction.EAST:
            new_position.x += 1

        if self._position.orientation.direction is Direction.SOUTH:
            new_position.y -= 1

        if self._position.orientation.direction is Direction.WEST:
            new_position.x -= 1

        # TODO: type hinting complains here because new_position is defined as an optional.
        # we check if new_position is set by calling the _is_placed() method earlier in this
        # function, but this is not picked up by the (Pyright) linter. Maybe there is a better
        # way to handle this?
        if self._table.valid_position(new_position):
            self._position = new_position
        else:
            logger.debug(
                "Preventing execution of MOVE command as it would cause "
                "the robot to fall off the table."
            )

    def _is_placed(self) -> bool:
        return self._position is not None
