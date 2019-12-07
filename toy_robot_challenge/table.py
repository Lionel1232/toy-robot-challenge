class Table:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def valid_position(self, position):
        return (0 <= position.x < self._length) and (0 <= position.y < self._width)
