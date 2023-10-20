from io import StringIO
from src.practice.practice_6.practice_6_task_1 import *
import pytest

test_quadratic_solver_array = [
    (4, -20, 25, [2.5]),
    (2, -14, 24, [3, 4]),
]

test_solve_array = [
    (4, -20, 25, [2.5]),
    (2, -14, 24, [3, 4]),
    (0, 3, 3, [-1]),
    (0, 3, 0, [0]),
    (0, 0, 0, []),
]

test_linear_solver_array = [(3, 3, [-1]), (3, 0, [0])]

test_is_float_number_array = [("2", True), ("2.3", True), ("a", False)]

test_string_to_float_array = [
    ("1 2 3", [1.0, 2.0, 3.0]),
    ("2.9 2 2.0", [2.9, 2.0, 2.0]),
]

test_check_user_input = [("1 2 3", 3, True), ("1 2 3 3", 3, False)]

test_main_scenario = [("2 -14 24", "3.0 4.0\n"), ("4 -20 25", "2.5\n")]

test_error_main_scenario = [("2 -14"), ("4 -20 25 12")]

test_error_quadratic_solver_array = [(1, 2, 3), (1, 2, 5), (10, 23, 100)]

test_error_solve_array = [(0, 0, 1), (0, 0, 12)]

test_error_string_to_float = [("a 2 3"), ("a v c")]


@pytest.mark.parametrize("a,b,c,expected", test_quadratic_solver_array)
def test_quadratic_solver(a, b, c, expected):
    assert quadratic_solver(a, b, c) == expected


@pytest.mark.parametrize("b,k,expected", test_linear_solver_array)
def test_linear_solver(b, k, expected):
    assert linear_solver(b, k) == expected


@pytest.mark.parametrize("num,expected", test_is_float_number_array)
def test_is_float_number(num, expected):
    assert is_float_number(num) is expected


@pytest.mark.parametrize("a,b,c,expected", test_solve_array)
def test_solve(a, b, c, expected):
    assert solve(a, b, c) == expected


@pytest.mark.parametrize("line,expected", test_string_to_float_array)
def test_string_to_float(line, expected):
    assert string_to_float(line) == expected


@pytest.mark.parametrize("line,number_of_elements,expected", test_check_user_input)
def test_check_user_input(line, number_of_elements, expected):
    assert check_user_input(line, number_of_elements) is expected


@pytest.mark.parametrize("user_input,expected", test_main_scenario)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected


@pytest.mark.parametrize("user_input", test_error_main_scenario)
def test_error_main_scenario(monkeypatch, user_input):
    with pytest.raises(ValueError):
        monkeypatch.setattr("builtins.input", lambda _: user_input)
        main()


@pytest.mark.parametrize("a,b,c", test_error_quadratic_solver_array)
def test_error_quadratic_solver(a, b, c):
    with pytest.raises(ValueError):
        quadratic_solver(a, b, c)


@pytest.mark.parametrize("a,b,c", test_error_solve_array)
def test_error_solve(a, b, c):
    with pytest.raises(ValueError):
        solve(a, b, c)


@pytest.mark.parametrize("line", test_error_string_to_float)
def test_error_string_to_float(line):
    with pytest.raises(ValueError):
        string_to_float(line)
