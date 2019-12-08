from toy_robot_challenge.positioning import Position


class Table:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def valid_position(self, position: Position) -> bool:
        return (0 <= position.x < self._length) and (0 <= position.y < self._width)
