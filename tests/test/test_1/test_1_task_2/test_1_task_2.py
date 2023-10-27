from src.test.test_1.test_1_task_2.list import *
import pytest


def create_example_list(insert_args):
    ls = create()
    for i in range(len(insert_args)):
        insert(ls, insert_args[i], i)
    return ls


@pytest.mark.parametrize("args,expected", [((0, 1, 2, 3), 0), ((1, 2, 3), 1)])
def test_head(args, expected):
    example_list = create_example_list(args)
    assert head(example_list) == expected


@pytest.mark.parametrize("args,expected", [((0, 1, 2, 3), 3), ((1, 2), 2)])
def test_tail(args, expected):
    example_list = create_example_list(args)
    assert tail(example_list) == expected


@pytest.mark.parametrize(
    "args,insert_argument,index,expected", [((0, 1, 2, 3), 4, 3, 3), ((1, 2), 3, 2, 3)]
)
def test_tail(args, insert_argument, index, expected):
    example_list = create_example_list(args)
    insert(example_list, insert_argument, index)
    assert tail(example_list) == expected


@pytest.mark.parametrize(
    "args,locate_argument,expected", [((0, 1, 2, 3), 3, 3), ((1, 2), 1, 0)]
)
def test_locate(args, locate_argument, expected):
    example_list = create_example_list(args)
    assert locate(example_list, locate_argument) == expected


@pytest.mark.parametrize(
    "args,retrieve_argument,expected", [((0, 1, 2, 3), 1, 1), ((1, 2), 1, 2)]
)
def test_retrieve(args, retrieve_argument, expected):
    example_list = create_example_list(args)
    assert retrieve(example_list, retrieve_argument) == expected


@pytest.mark.parametrize("args,index,expected", [((0, 1, 2, 3), 1, 2), ((1, 2), 0, 2)])
def test_delete(args, index, expected):
    example_list = create_example_list(args)
    delete(example_list, index)
    assert retrieve(example_list, index) == expected
