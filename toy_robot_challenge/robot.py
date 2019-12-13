import copy
import logging
from typing import Optional

from .positioning import Direction, Position, Turn
from .table import Table

logger = logging.getLogger(__name__)


class Robot:
    def __init__(self, table: Table):
        self._position: Optional[Position] = None
        self._table = table

    def place(self, x: int, y: int, direction: Direction) -> None:
        placement = Position(x, y, direction)
        if self._table.valid_position(placement):
            self._position = placement

    def report(self) -> None:
        if self._is_placed():
            logger.info(self._position)

    def rotate(self, turning_direction: Turn) -> None:
        if not self._is_placed():
            return
        self._position.direction = Direction[
            self._position.direction.value[turning_direction]
        ]

    def move(self) -> None:
        if not self._is_placed():
            return

        new_position = copy.copy(self._position)
        new_position.x += self._position.direction.dx
        new_position.y += self._position.direction.dy

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
