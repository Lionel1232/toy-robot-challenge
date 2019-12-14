import logging
import re
from enum import Enum

from .positioning import Direction, Turn

logger = logging.getLogger(__name__)


class Command(Enum):
    PLACE = "PLACE"
    MOVE = "MOVE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    REPORT = "REPORT"


class CommandProcessor:
    def __init__(self, robot):
        self._robot = robot

    def process(self, command):
        logger.debug(f"Processing command: {command}")
        try:
            command_type = Command[command.partition(" ")[0].upper()]
        except KeyError:
            logger.debug(f"Detected command as invalid. Terminating command execution.")
            return

        if command_type is Command.PLACE:
            arguments = re.findall(r"\d+,\d+,[A-Za-z]+", command)
            if not arguments:
                logger.debug(
                    "PLACE command invoked but the arguments provided were "
                    "invalid or missing (x,y,f). Terminating command execution."
                )
                return

            command_components = [
                component.upper().strip() for component in arguments[0].split(",")
            ]

            try:
                direction = Direction[command_components[2]]
            except KeyError:
                logger.debug(
                    "Invalid direction provided in PLACE command. "
                    "Terminating command execution."
                )
                return

            x = int(command_components[0])
            y = int(command_components[1])

            self._robot.place(x, y, direction)
            logger.debug("Finished executing PLACE command.")
            return

        if command_type is Command.REPORT:
            self._robot.report()
            logger.debug("Finished executing REPORT command.")
            return

        if command_type in [Command.LEFT, Command.RIGHT]:
            self._robot.rotate(Turn[command_type.value])
            logger.debug("Finished executing LEFT/RIGHT command.")
            return

        if command_type is Command.MOVE:
            self._robot.move()
            logger.debug("Finished executing MOVE command.")
            return
