from dataclasses import dataclass

from toy_robot_challenge.positioning import Position


@dataclass
class Table:
    _length: int
    _width: int

    def valid_position(self, position: Position) -> bool:
        return (0 <= position.x < self._length) and (0 <= position.y < self._width)
