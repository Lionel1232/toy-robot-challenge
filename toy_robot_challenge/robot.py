import copy
import functools
import logging
from typing import Optional

from .positioning import Direction, Position, Turn
from .table import Table

logger = logging.getLogger(__name__)


def check_if_placed(func):
    @functools.wraps(func)
    def wrapper(self, *args):
        if self._is_placed():
            return func(self, *args)

    return wrapper


class Robot:
    def __init__(self, table: Table):
        self._position: Optional[Position] = None
        self._table = table

    def place(self, x: int, y: int, direction: Direction) -> None:
        placement = Position(x, y, direction)
        if self._table.valid_position(placement):
            self._position = placement

    @check_if_placed
    def report(self) -> None:
        logger.info(str(self._position))

    @check_if_placed
    def rotate(self, turning_direction: Turn) -> None:
        self._position.direction = Direction[
            self._position.direction.value[turning_direction]
        ]

    @check_if_placed
    def move(self) -> None:
        new_position = copy.copy(self._position)
        new_position.x += self._position.direction.dx
        new_position.y += self._position.direction.dy

        assert new_position is not None
        if self._table.valid_position(new_position):
            self._position = new_position
        else:
            logger.debug(
                "Preventing execution of MOVE command as it would cause "
                "the robot to fall off the table."
            )

    def _is_placed(self) -> bool:
        return self._position is not None
