from toy_robot_challenge.positioning import Direction, Orientation, Position, Turn


def test_create_position(mocker):
    mock_orientation = mocker.Mock()
    position = Position(1, 1, mock_orientation)

    assert position.x == 1
    assert position.y == 1
    assert position.orientation == mock_orientation


def test_position_string_representation_is_accurate(mocker):
    mock_orientation = mocker.Mock()
    mock_orientation.direction.value = "NORTH"
    position = Position(1, 1, mock_orientation)

    assert str(position) == "1,1,NORTH"


def test_create_orientation():
    orientation = Orientation(Direction.NORTH, Direction.WEST, Direction.EAST)

    assert orientation.direction == Direction.NORTH
    assert orientation._left == Direction.WEST
    assert orientation._right == Direction.EAST


def test_get_direction_returns_correct_direction_for_turn():
    orientation = Orientation(Direction.NORTH, Direction.WEST, Direction.EAST)

    assert orientation.get_direction(Turn.LEFT) == Direction.WEST
    assert orientation.get_direction(Turn.RIGHT) == Direction.EAST
