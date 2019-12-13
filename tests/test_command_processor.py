import logging
from toy_robot_challenge.robot import Robot

import pytest

from toy_robot_challenge.command_processor import CommandProcessor
from toy_robot_challenge.positioning import Direction, Turn


@pytest.fixture()
def mock_robot(mocker):
    return mocker.create_autospec(Robot, instance=True)


def test_create_command_processor(mock_robot):
    command_processor = CommandProcessor(mock_robot)

    assert command_processor._robot == mock_robot


def test_process_ignores_invalid_command(caplog, mock_robot):
    caplog.set_level(logging.DEBUG)
    command_processor = CommandProcessor(mock_robot)

    command_processor.process("invalid-command")

    assert mock_robot.place.called is False
    assert mock_robot.report.called is False
    assert mock_robot.rotate.called is False
    assert mock_robot.move.called is False
    assert "Detected command as invalid. Terminating command execution." in str(
        caplog.records
    )


@pytest.mark.parametrize(
    "command", ["PLACE", "PLACE 1,2", "PLACE 1,NORTH,1", "PLACE 1,2,3", "PLACE NORTH"]
)
def test_process_does_not_place_robot_for_place_command_with_missing_place_arguments(
    caplog, mock_robot, command
):
    caplog.set_level(logging.DEBUG)
    command_processor = CommandProcessor(mock_robot)

    command_processor.process(command)

    assert mock_robot.place.called is False
    assert mock_robot.report.called is False
    assert mock_robot.rotate.called is False
    assert mock_robot.move.called is False
    assert (
        "PLACE command invoked but the arguments provided were invalid or missing (x,y,f)."
        in str(caplog.records)
    )


def test_process_does_not_place_robot_for_place_command_with_invalid_direction(
    caplog, mock_robot
):
    caplog.set_level(logging.DEBUG)
    command_processor = CommandProcessor(mock_robot)

    command_processor.process("PLACE 1,2,invalid")

    assert mock_robot.place.called is False
    assert mock_robot.report.called is False
    assert mock_robot.rotate.called is False
    assert mock_robot.move.called is False
    assert "Invalid direction provided in PLACE command." in str(caplog.records)


def test_process_places_robot_for_valid_place_command(mock_robot):
    command_processor = CommandProcessor(mock_robot)

    command_processor.process("PLACE 1,2,NORTH")

    mock_robot.place.assert_called_once_with(1, 2, Direction.NORTH)
    assert mock_robot.report.called is False
    assert mock_robot.rotate.called is False
    assert mock_robot.move.called is False


def test_process_tells_robot_to_report_for_report_command(mock_robot):
    command_processor = CommandProcessor(mock_robot)

    command_processor.process("REPORT")

    assert mock_robot.report.called is True
    assert mock_robot.place.called is False
    assert mock_robot.rotate.called is False
    assert mock_robot.move.called is False


@pytest.mark.parametrize("command, turn", [("LEFT", Turn.LEFT), ("RIGHT", Turn.RIGHT)])
def test_process_tells_robot_to_rotate_for_left_or_right_command(
    mock_robot, command, turn
):
    command_processor = CommandProcessor(mock_robot)

    command_processor.process(command)

    mock_robot.rotate.assert_called_once_with(turn)
    assert mock_robot.report.called is False
    assert mock_robot.place.called is False
    assert mock_robot.move.called is False


def test_process_tells_robot_to_move_for_move_command(mock_robot):
    command_processor = CommandProcessor(mock_robot)

    command_processor.process("MOVE")

    assert mock_robot.move.called is True
    assert mock_robot.report.called is False
    assert mock_robot.place.called is False
    assert mock_robot.rotate.called is False
