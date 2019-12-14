import pytest

from toy_robot_challenge.positioning import Direction, Position


def test_create_position(mocker):
    position = Position(1, 1, Direction.NORTH)

    assert position.x == 1
    assert position.y == 1
    assert position.direction == Direction.NORTH


def test_position_string_representation_is_accurate(mocker):
    position = Position(1, 1, Direction.NORTH)

    assert str(position) == "1,1,NORTH"


@pytest.mark.parametrize(
    "direction, expected_offset",
    [
        (Direction.NORTH, 0),
        (Direction.EAST, 1),
        (Direction.SOUTH, 0),
        (Direction.WEST, -1),
    ],
)
def test_direction_property_dx_returns_accurate_movement_offset_for_direction(
    direction, expected_offset
):
    assert direction.dx == expected_offset


@pytest.mark.parametrize(
    "direction, expected_offset",
    [
        (Direction.NORTH, 1),
        (Direction.EAST, 0),
        (Direction.SOUTH, -1),
        (Direction.EAST, 0),
    ],
)
def test_direction_property_dy_returns_accurate_movement_offset_for_direction(
    direction, expected_offset
):
    assert direction.dy == expected_offset


@pytest.mark.parametrize(
    "initial_direction, expected_left, expected_right",
    [
        (Direction.NORTH, Direction.WEST, Direction.EAST),
        (Direction.EAST, Direction.NORTH, Direction.SOUTH),
        (Direction.SOUTH, Direction.EAST, Direction.WEST),
        (Direction.WEST, Direction.SOUTH, Direction.NORTH),
    ],
)
def test_direction_properties_left_and_right_return_accurate_direction(
    initial_direction, expected_left, expected_right
):
    assert initial_direction.left is expected_left
    assert initial_direction.right is expected_right
