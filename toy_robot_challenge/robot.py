import copy
import logging

from toy_robot_challenge.positioning import Direction, Orientation, Position

logger = logging.getLogger(__name__)


class Robot:
    def __init__(self, table):
        self._position = None
        self._table = table
        self._orientations = {
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

    def place(self, x, y, direction):
        placement = Position(x, y, self._orientations[direction])
        if self._table.valid_position(placement):
            self._position = placement

    def report(self):
        if self._is_placed():
            logger.info(self._position)

    def rotate(self, turning_direction):
        if not self._is_placed():
            return

        self._position.orientation = self._orientations[
            self._position.orientation.get_direction(turning_direction)
        ]

    def move(self):
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

        if self._table.valid_position(new_position):
            self._position = new_position
        else:
            logger.debug(
                "Preventing execution of MOVE command as it would cause "
                "the robot to fall off the table."
            )

    def _is_placed(self):
        return self._position is not None
