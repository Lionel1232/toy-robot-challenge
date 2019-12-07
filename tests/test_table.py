import pytest

from toy_robot_challenge.positioning import Direction, Position
from toy_robot_challenge.table import Table


def test_create_table():
    length = 5
    width = 3
    table = Table(length, width)

    assert table._length == length
    assert table._width == width


@pytest.mark.parametrize("x, y", [(-1, 0), (0, -1), (-1, -1), (5, 5), (6, 5), (5, 6)])
def test_valid_position_returns_false_for_invalid_position(x, y):
    table = Table(5, 5)
    position = Position(x, y, Direction.NORTH)

    assert table.valid_position(position) is False


@pytest.mark.parametrize("x, y", [(0, 0), (4, 4), (3, 3)])
def test_valid_position_returns_true_for_valid_position(x, y):
    table = Table(5, 5)
    position = Position(x, y, Direction.NORTH)

    assert table.valid_position(position) is True
