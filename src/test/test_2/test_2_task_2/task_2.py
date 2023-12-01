import time
from functools import wraps
from inspect import getcallargs
from os import makedirs
from os.path import exists


def logger(output_file_name: str):
    if not exists(output_file_name):
        directory = "/".join(output_file_name.split("/")[:-1])
        if directory:
            makedirs(directory)
    with open(output_file_name, "w"):
        pass

    def decor(func):
        @wraps(func)
        def inner(*args, **kwargs):
            true_order = getcallargs(func, *args, *kwargs.values())
            argument_names = getcallargs(func, *args, **kwargs)

            for key in true_order.keys():
                true_order[key] = argument_names[key]

            date_time = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
            true_order = " ".join(
                map(
                    lambda key_value: "{0}={1}".format(*key_value),
                    zip(true_order.keys(), true_order.values()),
                )
            )

            result = func(*args, **kwargs)
            output_line = f"{date_time} {func.__name__} {true_order} {result}\n"

            with open(output_file_name, "a") as output_file:
                output_file.write(output_line)

            return result

        return inner

    return decor


@logger("test_folder/logs.txt")
def foo(a, b=2, c=3):
    print(a, b, c)


if __name__ == "__main__":
    foo(100)
    foo(b=10, a=2, c=3)
