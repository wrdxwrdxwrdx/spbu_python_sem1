from src.test.test_2.task_2 import *


@safe_call
def error_func_1():
    return 12 / 0


@safe_call
def error_func_2():
    return str(1) + 1


@safe_call
def error_func_3():
    return str(12) / 2


@safe_call
def error_func_4():
    def foo():
        return 12 - str(1)

    return foo()


@safe_call
def error_func_5():
    def foo():
        array = [1, 2, 3]
        return array[10]

    return foo()


@safe_call
def correct_func_1():
    def foo():
        array = [1, 2, 3]
        return array[1]

    return foo()


@safe_call
def correct_func_1():
    def foo():
        array = [1, 2, 3]
        return array[1]

    return foo()


@safe_call
def correct_func_2():
    return 1 + 2


@safe_call
def correct_func_3():
    return 2 / 1


@safe_call
def correct_func_4():
    return int(str(12))
