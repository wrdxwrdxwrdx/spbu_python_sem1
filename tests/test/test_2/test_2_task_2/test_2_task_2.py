from tests.test.test_2.test_2_task_2.functions_file import *
import pytest


@pytest.mark.parametrize(
    "function,expected",
    [
        (
            error_func_1,
            "ZeroDivisionError in line 6\n"
            "function_name: error_func_1\n"
            "line 6: return 12 / 0",
        ),
        (
            error_func_2,
            "TypeError in line 11\n"
            "function_name: error_func_2\n"
            "line 11: return str(1) + 1",
        ),
        (
            error_func_3,
            "TypeError in line 16\n"
            "function_name: error_func_3\n"
            "line 16: return str(12) / 2",
        ),
        (
            error_func_4,
            "TypeError in line 22\n"
            "function_name: foo\n"
            "line 22: return 12 - str(1)",
        ),
        (
            error_func_5,
            "IndexError in line 31\n"
            "function_name: foo\n"
            "line 31: return array[10]",
        ),
    ],
)
def test_get_error_info(function, expected):
    try:
        function
    except Exception as error:
        assert get_error_info(error) == expected


@pytest.mark.parametrize(
    "function",
    [correct_func_1, correct_func_2, correct_func_3, correct_func_4],
)
def test_safe_call_correct(function):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        function()
        assert len(w) == 0


@pytest.mark.parametrize(
    "function,expected_message",
    [
        (
            error_func_1,
            "ZeroDivisionError in line 6\n"
            "function_name: error_func_1\n"
            "line 6: return 12 / 0",
        ),
        (
            error_func_2,
            "TypeError in line 11\n"
            "function_name: error_func_2\n"
            "line 11: return str(1) + 1",
        ),
        (
            error_func_3,
            "TypeError in line 16\n"
            "function_name: error_func_3\n"
            "line 16: return str(12) / 2",
        ),
        (
            error_func_4,
            "TypeError in line 22\n"
            "function_name: foo\n"
            "line 22: return 12 - str(1)",
        ),
        (
            error_func_5,
            "IndexError in line 31\n"
            "function_name: foo\n"
            "line 31: return array[10]",
        ),
    ],
)
def test_safe_call_error(function, expected_message):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        assert function() is None
        assert len(w) != 0
        assert issubclass(w[-1].category, Warning)
        assert str(w[-1].message) == expected_message
