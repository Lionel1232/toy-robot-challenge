import pytest

from toy_robot_challenge.positioning import Direction, Position, Turn
from toy_robot_challenge.robot import Robot


def test_create_robot(mocker):
    mock_table = mocker.Mock()
    robot = Robot(mock_table)

    assert robot._position is None
    assert robot._table is mock_table


def test_place_sets_position_for_valid_position_on_table(mocker):
    mock_table = mocker.Mock()
    mock_placement = mocker.Mock()
    mock_position = mocker.patch(
        "toy_robot_challenge.robot.Position", return_value=mock_placement, autospec=True
    )
    mock_table.valid_position.return_value = True

    robot = Robot(mock_table)
    robot.place(1, 1, Direction.NORTH)

    mock_position.assert_called_once_with(1, 1, Direction.NORTH)
    mock_table.valid_position.assert_called_once_with(mock_placement)
    assert robot._position is mock_placement


def test_place_does_not_set_position_for_invalid_position_on_table(mocker):
    mock_table = mocker.Mock()
    mock_placement = mocker.Mock()
    mock_position = mocker.patch(
        "toy_robot_challenge.robot.Position", return_value=mock_placement, autospec=True
    )
    mock_table.valid_position.return_value = False

    robot = Robot(mock_table)
    robot.place(1, 1, Direction.NORTH)

    mock_position.assert_called_once_with(1, 1, Direction.NORTH)
    mock_table.valid_position.assert_called_once_with(mock_placement)
    assert robot._position is None


def test_is_placed_returns_true_when_robot_has_valid_position(mocker):
    robot = Robot(mocker.Mock())

    robot._position = mocker.Mock()

    assert robot._is_placed() is True


def test_is_placed_returns_false_when_robot_has_None_position(mocker):
    mock_table = mocker.Mock()
    robot = Robot(mock_table)

    assert robot._is_placed() is False


def test_report_does_not_report_position_if_robot_is_not_placed(mocker):
    mock_logger = mocker.patch("toy_robot_challenge.robot.logger")
    robot = Robot(mocker.Mock())
    mocker.patch.object(robot, "_is_placed", return_value=False)

    # mock robot._position to avoid having to assert that the logger was called with `None`
    mock_position = mocker.Mock()
    robot._position = mock_position
    robot.report()

    assert mock_logger.info.called is False


def test_report_calls_logger_with_position_if_robot_is_placed(mocker):
    mock_logger = mocker.patch("toy_robot_challenge.robot.logger")
    robot = Robot(mocker.Mock())
    mocker.patch.object(robot, "_is_placed", return_value=True)

    # mock robot._position to avoid having to assert that the logger was called with `None`
    mock_position = mocker.Mock()
    robot._position = mock_position
    robot.report()

    mock_logger.info.assert_called_once_with(str(mock_position))


def test_rotate_does_not_change_orientation_of_robot_if_not_placed(mocker):
    robot = Robot(mocker.Mock())
    robot._position = mocker.Mock(direction=Direction.NORTH)
    mocker.patch.object(robot, "_is_placed", return_value=False)

    robot.rotate(Turn.LEFT)

    assert robot._position.direction == Direction.NORTH


def test_rotate_changes_orientation_of_robot(mocker):
    robot = Robot(mocker.Mock())
    robot._position = Position(0, 0, Direction.NORTH)

    robot.rotate(Turn.LEFT)

    assert robot._position.direction == Direction.WEST


@pytest.mark.parametrize(
    "initial_position, initial_direction, expected_position, expected_direction",
    [
        ((0, 0), Direction.NORTH, (0, 1), Direction.NORTH),
        ((5, 5), Direction.SOUTH, (5, 4), Direction.SOUTH),
        ((0, 0), Direction.EAST, (1, 0), Direction.EAST),
        ((2, 2), Direction.WEST, (1, 2), Direction.WEST),
    ],
)
def test_move_changes_position_of_robot_to_correct_location_for_valid_new_position(
    mocker, initial_position, initial_direction, expected_position, expected_direction
):
    robot = Robot(mocker.Mock())
    robot._table.valid_position.return_value = True
    initial_x, initial_y = initial_position
    starting_position = Position(initial_x, initial_y, initial_direction)
    robot._position = starting_position

    robot.move()

    # TODO: test if `valid_position` was actually called with the correct position
    robot._table.valid_position.assert_called_once()
    assert (robot._position.x, robot._position.y) == expected_position
    assert robot._position.direction == expected_direction


def test_move_does_not_move_robot_robot_for_invalid_new_position(mocker, caplog):
    robot = Robot(mocker.Mock())
    robot._table.valid_position.return_value = False
    initial_x, initial_y = 0, 0
    starting_position = Position(initial_x, initial_y, direction=Direction.SOUTH)
    robot._position = starting_position

    robot.move()

    assert robot._table.valid_position.called is True
    assert (robot._position.x, robot._position.y) == (initial_x, initial_y)
    assert robot._position.direction == Direction.SOUTH
    assert "Preventing execution of MOVE command as it would cause "
    "the robot to fall off the table." in str(caplog.records)


def test_move_does_not_change_position_of_robot_if_robot_is_not_placed(mocker):
    robot = Robot(mocker.Mock())
    mocker.patch.object(robot, "_position", "fake-position")
    mocker.patch.object(robot, "_is_placed", return_value=False)

    robot.move()

    assert robot._position == "fake-position"
    robot._table.valid_position.assert_not_called()
