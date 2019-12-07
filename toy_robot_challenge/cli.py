import logging
import sys

import click

from toy_robot_challenge.command_processor import CommandProcessor
from toy_robot_challenge.robot import Robot
from toy_robot_challenge.table import Table

# setup the root logger
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@click.command()
@click.argument("input_file", type=click.File("r"), required=False)
@click.option(
    "-v", "--verbosity", type=click.Choice(["OFF", "INFO", "DEBUG"]), default="INFO"
)
def main(input_file, verbosity):  # noqa
    logger.setLevel(verbosity)
    table = Table(5, 5)
    robot = Robot(table)
    command_processor = CommandProcessor(robot)

    if input_file:
        logger.debug(f"Reading commands in input file {input_file.name}")
        for command in input_file.readlines():
            command_processor.process(command.strip())
        return 0

    logger.debug(f"Reading commands from stdin")
    for command in sys.stdin:
        command_processor.process(command.strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
