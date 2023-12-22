from typing import Callable
from functools import wraps
import warnings
import traceback


def get_error_info(error: Exception) -> str:
    error_type = type(error).__name__

    traceback_text = traceback.format_exc().strip().split("\n")
    error_info = traceback_text[-3].split()

    line_number = (error_info[-3])[:-1]
    function_name = error_info[-1]
    code_line = traceback_text[-2].strip()

    warning_output = (
        f"{error_type} in line {line_number}\n"
        f"function_name: {function_name}\n"
        f"line {line_number}: {code_line}"
    )
    return warning_output


def safe_call(func: Callable):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            warning_output = get_error_info(error)
            warnings.warn(Warning(warning_output), stacklevel=2)

            return None

    return inner
