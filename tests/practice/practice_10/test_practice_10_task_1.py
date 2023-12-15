from io import StringIO

from src.practice.practice_10.practice_10_task_1 import *
import pytest


@pytest.mark.parametrize(
    "file_name",
    [
        ("test_files/test_1.txt"),
        ("test_files/test_2.txt"),
        ("test_files/test_3.txt"),
        ("test_files/test_4.txt"),
        ("test_files/test_5.txt"),
        ("test_files/test_6.txt"),
    ],
)
def test_main_scenario(monkeypatch, file_name):
    with open(file_name, "r") as file:
        user_input = file.readline()
        expected = file.readlines()
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == "".join(expected)
