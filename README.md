# Toy-Robot-Challenge

A Python application that simulates a toy robot moving around on a 5 x 5 table.

## Installation

First, clone the project and navigate to the project root.

To install the application using pip:

- Run: `pip install .`.
- The application can now be started using the `toy_robot` command.

To install the application for local development:

- Create a virtual environment: `python -m venv venv` or `tox`.
- Activate the environment: `source venv/bin/activate`.
- Install the dependencies: `pip install requirements.txt`.
- To run the application, execute `python -m toy_robot_challenge.cli` from the project root.

## Usage

### Available Commands

See [the problem statement](PROBLEM.md) for rules on how the robot is able to operate.

The following commands can be issued to the robot (commands are case insensitive):

- `PLACE <x>,<y>,<direction>` This will place the robot on the table. Valid directions are: `north, south, east, west`.
- `MOVE` This will move the robot 1 square in the direction it is facing.
- `LEFT` & `RIGHT` This will rotate the robot by 90 degrees, changing the direction it is facing.
- `REPORT` This will print a report of the robot's current location to the terminal.

### Optional Arguments

```
Usage: toy_robot [OPTIONS] [INPUT_FILE]

Options:
  -v, --verbosity [OFF|INFO|DEBUG] (defaults to INFO)
  --help                          Show this message and exit.
```

> Note: If the application has not been installed via pip, these arguments can still be provided when running the `python -m toy_robot_challenge.cli` command.

### Input File Format

The input file should list individual commands seperated with a newline as shown in the [sample_command_sequence.txt](sample_command_sequence.txt) file included with this project. i.e

```
PLACE 1,1,NORTH
REPORT
MOVE
REPORT
RIGHT
MOVE
LEFT
REPORT
```

## Executing Tests

Tests are orchestrated using [Tox](https://tox.readthedocs.io/en/latest/), install this tool using `pip install tox` if you do not already have it.

- To run the test suite, execute the `tox` command.
- This will execute tests using [pytest](https://docs.pytest.org/en/latest/), creating a virtual environment containing all required dependencies if one does not already exist.
- If you wish to supply additional arguments when running pytest, you can supply them as additional positional arguments i.e `tox -e py38 -- -x -k test_robot`.
