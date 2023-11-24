from io import StringIO
from src.test.test_2.task_2 import *
import pytest


def func_no_decorator():
    pass


@spy
def dummy_function():
    pass


def test_print_usage_statistic():
    value = [i for i in print_usage_statistic(dummy_function)]
    assert "".join(value) == ""


def test_main_scenario(monkeypatch):
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    start_time = time.strftime("%H:%M:%S", time.localtime())
    expected = (
        f"30\n"
        f"hello\n"
        f"5\n"
        f"10\n"
        f"hello world\n"
        f"function foo was called at {start_time} with parameters:\n"
        f"num = 30\n"
        f"function foo was called at {start_time} with parameters:\n"
        f"num = hello\n"
        f"function foo was called at {start_time} with parameters:\n"
        f"num = 5\n"
        f"function goo was called at {start_time} with parameters:\n"
        f"num = 10\n"
        f"function goo was called at {start_time} with parameters:\n"
        f"num = hello world\n"
    )
    main()

    output = fake_output.getvalue()
    assert output.split("\n") == expected.split("\n")


def test_error_check_code():
    with pytest.raises(AttributeError):
        check_code(func_no_decorator())
