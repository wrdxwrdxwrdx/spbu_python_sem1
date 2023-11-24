import time
import functools
from inspect import getcallargs


def spy(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.strftime("%H:%M:%S", time.localtime())
        argument_names = getcallargs(func, *args, **kwargs)
        inner.logs.setdefault(func.__name__, []).append((start_time, argument_names))

        return func(*args, **kwargs)

    inner.logs = {}

    return inner


def print_usage_statistic(func):
    check_code(func)

    for info in func.logs[func.__name__]:
        yield info


@spy
def foo(num) -> None:
    print(num)


@spy
def goo(num) -> None:
    print(num)


def check_code(func):
    try:
        func.logs[func.__name__]
    except AttributeError:
        raise AttributeError(
            f"function {func.__name__} with out decorator spy"
        ) from None
    except KeyError:
        func.logs[func.__name__] = {}


def user_output(func) -> None:
    for times, parameters in print_usage_statistic(func):
        str_parameters = ", ".join(f"{k} = {v}" for k, v in parameters.items())
        print(
            f"function {func.__name__} was called at {times} "
            f"with parameters:\n{str_parameters}"
        )


def main() -> None:
    foo(30)
    foo("hello")
    foo(5)
    goo(10)
    goo("hello world")

    user_output(foo)
    user_output(goo)


if __name__ == "__main__":
    main()
