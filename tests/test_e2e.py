from click.testing import CliRunner

from toy_robot_challenge.cli import main


def test_toy_robot_e2e(caplog):
    input = """
    MOVE\n
    REPORT\n
    PLACE 1,1,NORTH\n
    REPORT\n
    MOVE\n
    REPORT\n
    RIGHT\n
    REPORT\n
    MOVE\n
    LEFT\n
    MOVE\n
    move\n
    move\n
    move\n
    report\n
    move\n
    report\n
    """

    runner = CliRunner()
    result = runner.invoke(main, input=input)

    assert result.exit_code == 0

    assert "1,1,NORTH" in caplog.records[0].message
    assert "1,2,NORTH" in caplog.records[1].message
    assert "1,2,EAST" in caplog.records[2].message
    assert "2,4,NORTH" in caplog.records[3].message
    assert "2,4,NORTH" in caplog.records[4].message
