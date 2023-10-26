from io import StringIO
from src.practice.practice_6.practice_6_task_1 import *
import pytest


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (4, -20, 25, (2.5,)),
        (2, -14, 24, (3.0, 4.0)),
    ],
)
def test_quadratic_solver(a, b, c, expected):
    assert (
        quadratic_solver(a, b, c) == expected
        or quadratic_solver(a, b, c) == expected[::-1]
    )


@pytest.mark.parametrize("b,k,expected", [(3, 3, (-1.0,)), (3, 0, (0.0,))])
def test_linear_solver(b, k, expected):
    assert linear_solver(b, k) == expected


@pytest.mark.parametrize("num,expected", [("2", True), ("2.3", True), ("a", False)])
def test_is_float_number(num, expected):
    assert is_float_number(num) == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (4, -20, 25, (2.5,)),
        (2, -14, 24, (3.0, 4.0)),
        (0, 3, 3, (-1,)),
        (0, 3, 0, (0,)),
    ],
)
def test_solve(a, b, c, expected):
    assert solve(a, b, c) == expected or solve(a, b, c) == expected[::-1]


@pytest.mark.parametrize(
    "line,expected",
    [
        ("1 2 3", (1.0, 2.0, 3.0)),
        ("2.9 2 2.0", (2.9, 2.0, 2.0)),
    ],
)
def test_string_to_float(line, expected):
    assert string_to_float(line) == expected


@pytest.mark.parametrize(
    "line,number_of_elements,expected", [("1 2 3", 3, True), ("1 2 4", 3, True)]
)
def test_check_user_input(line, number_of_elements, expected):
    assert check_user_input(line, number_of_elements) == expected


@pytest.mark.parametrize(
    "user_input,expected", [("2 -14 24", "3.0 4.0\n"), ("4 -20 25", "2.5\n")]
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert (
        output.split() == expected.split() or output.split() == expected.split()[::-1]
    )


@pytest.mark.parametrize("a,b,c", [(1, 2, 3), (1, 2, 5), (10, 23, 100)])
def test_error_quadratic_solver(a, b, c):
    with pytest.raises(ValueError):
        quadratic_solver(a, b, c)


@pytest.mark.parametrize("a,b,c", [(0, 0, 1), (0, 0, 12), (0, 0, 0)])
def test_error_solve(a, b, c):
    with pytest.raises(ValueError):
        solve(a, b, c)


@pytest.mark.parametrize("line", [("a 2 3"), ("a v c")])
def test_error_string_to_float(line):
    with pytest.raises(ValueError):
        string_to_float(line)


@pytest.mark.parametrize("line,k", [("1 2 3 4", 3), ("1 2", 3)])
def test_error_check_user_input(line, k):
    with pytest.raises(ValueError):
        check_user_input(line, k)


@pytest.mark.parametrize("k,b", [(0, 3), (0, 2)])
def test_error_linear_solver(k, b):
    with pytest.raises(ValueError):
        linear_solver(k, b)
