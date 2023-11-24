from src.test.test_2.task_1 import *
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "number,expected",
    [(0, 0), (1, 1), (2, 1), (3, 2), (6, 8), (23, 28657), (90, 2880067194370816120)],
)
def test_fibonacci(number, expected):
    assert fibonacci(number) == expected


@pytest.mark.parametrize(
    "user_input",
    ["number", "asd", "12.3", "a123", "-1", "100"],
)
def test_error_check_input(user_input):
    with pytest.raises(ValueError):
        check_input(user_input)


@pytest.mark.parametrize(
    "user_input",
    ["12", "13", "0", "012", "88", "90"],
)
def test_error_check_input(user_input):
    assert check_input(user_input) is None


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("1", "1-st element is 1"),
        ("2", "2-nd element is 1"),
        ("3", "3-rd element is 2"),
        ("4", "4-th element is 3"),
        ("12", "12-th element is 144"),
        ("33", "33-th element is 3524578"),
        ("90", "90-th element is 2880067194370816120"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output.split() == expected.split()


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("-1", "number must be from 0 to 90"),
        ("asd", "You entered not number"),
        ("123.3", "number must be Integer"),
        ("4", "4-th element is 3"),
        ("100", "number must be from 0 to 90"),
    ],
)
def test_error_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output.split() == expected.split()
