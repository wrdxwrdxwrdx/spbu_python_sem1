import pytest

from src.practice.practice_8.practice_8_task_1.hash_table import *


def dummy_hash_table(elements: tuple):
    hash_table = create_hash_table()
    for i in elements:
        put(hash_table, i[0], i[1])
    return hash_table


def test_create_hash_table():
    has_table = create_hash_table()
    assert isinstance(has_table, HashTable)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 5", 12),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 6", 13),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 12", 10),
    ],
)
def test_hash_function(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    assert hash_function(key, hash_table.capacity) == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), 4 / 16),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3)), 3 / 16),
        (
            (("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4), ("may 5", 5)),
            5 / 16,
        ),
        ((), 0),
    ],
)
def test_get_load_factor(elements, expected):
    hash_table = dummy_hash_table(elements)
    assert get_load_factor(hash_table) == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), 32),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), 32),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), 32),
        (
            (
                ("may 1", 1),
                ("may 2", 2),
                ("may 3", 3),
                ("may 4", 4),
                ("may 5", 5),
                ("may 6", 6),
                ("may 7", 7),
                ("may 8", 8),
                ("may 9", 9),
                ("may 10", 10),
                ("may 11", 11),
                ("may 12", 12),
                ("may 13", 13),
                ("may 14", 14),
            ),
            64,
        ),
    ],
)
def test_resize(elements, expected):
    hash_table = dummy_hash_table(elements)
    resize(hash_table)
    assert hash_table.capacity == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 4", 4),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 3", 3),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 1", 1),
    ],
)
def test_remove(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    keys_number = hash_table.keys_number
    assert remove(hash_table, key) == expected and (
        keys_number - hash_table.keys_number == 1
    )


@pytest.mark.parametrize(
    "elements,key",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 123"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 23"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 5"),
    ],
)
def test_error_remove(elements, key):
    hash_table = dummy_hash_table(elements)
    with pytest.raises(ValueError):
        remove(hash_table, key)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 4", 4),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 3", 3),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 1", 1),
    ],
)
def test_get(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    assert get(hash_table, key) == expected


@pytest.mark.parametrize(
    "elements,key",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 123"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 23"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 5"),
    ],
)
def test_error_get(elements, key):
    hash_table = dummy_hash_table(elements)
    with pytest.raises(ValueError):
        get(hash_table, key)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 4", True),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 3", True),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 11", False),
    ],
)
def test_has_key(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    assert has_key(hash_table, key) == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        (
            (("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)),
            [("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)],
        ),
        ((("may 1", 1), ("may 2", 2)), [("may 1", 1), ("may 2", 2)]),
        ((), []),
    ],
)
def test_items(elements, expected):
    hash_table = dummy_hash_table(elements)
    assert sorted(items(hash_table)) == sorted(expected)


@pytest.mark.parametrize(
    "elements,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), False),
        ((("may 1", 1), ("may 2", 2)), False),
        ((), False),
    ],
)
def test_get(elements, expected):
    hash_table = dummy_hash_table(elements)
    delete_hash_table(hash_table)
    assert bool(items(hash_table)) == expected
