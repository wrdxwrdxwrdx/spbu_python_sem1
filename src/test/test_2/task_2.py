import sys
from typing import Callable
from functools import wraps
import warnings
import traceback


def get_error_info(error: Exception) -> str:
    error_type = type(error).__name__

    exception_info = sys.exc_info()[2]
    exception_info_parsed = traceback.extract_tb(exception_info)[-1]
    function_name = exception_info_parsed.name
    line_number = exception_info_parsed.lineno
    code_line = exception_info_parsed.line

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
