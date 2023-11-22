from src.homeworks.homework_6.AVL_Tree import *
import pytest


def dummy_avl_tree(elements: tuple) -> TreeMap:
    avl_tree = create_tree_map()
    for key_value in elements:
        put(avl_tree, *key_value)
    return avl_tree


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 1, 1),
        (((1, 1), (2, 2), (3, 3), (4, 4)), 2, 2),
        (((1, 1), (2, 2), (3, 3), (4, 4)), 4, 4),
        (((1, 1),), 1, 1),
    ],
)
def test_get(elements, key, expected):
    avl_tree = dummy_avl_tree(elements)
    assert get(avl_tree, key) == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 1, True),
        (((1, 1), (2, 2), (3, 3), (4, 4)), 2, True),
        (((1, 1), (2, 2), (3, 3), (4, 4)), 4, True),
        (((1, 1), (2, 2), (3, 3), (4, 4)), 5, False),
        (((1, 1),), 3, False),
        (((1, 1),), 1, True),
    ],
)
def test_has_key(elements, key, expected):
    avl_tree = dummy_avl_tree(elements)
    assert has_key(avl_tree, key) == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 1),
        (((2, 2), (3, 3), (4, 4)), 2),
        (((5, 5),), 5),
    ],
)
def test_get_minimum(elements, expected):
    avl_tree = dummy_avl_tree(elements)
    assert get_minimum(avl_tree) == expected


@pytest.mark.parametrize(
    "elements,expected",
    [
        (((1, 1), (2, 2), (3, 3)), 3),
        (((2, 2), (3, 3), (4, 4)), 4),
        (((5, 5),), 5),
    ],
)
def test_get_maximum(elements, expected):
    avl_tree = dummy_avl_tree(elements)
    assert get_maximum(avl_tree) == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 3, 4),
        (((2, 2), (3, 3), (4, 4), (5, 5)), 4, 5),
        (((5, 5),), 3, 5),
    ],
)
def test_get_upper_bound(elements, key, expected):
    avl_tree = dummy_avl_tree(elements)
    assert get_upper_bound(avl_tree, key) == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 3, 3),
        (((2, 2), (3, 3), (4, 4), (5, 5)), 4, 4),
        (((5, 5),), 3, 5),
    ],
)
def test_get_lower_bound(elements, key, expected):
    avl_tree = dummy_avl_tree(elements)
    assert get_lower_bound(avl_tree, key) == expected


@pytest.mark.parametrize(
    "elements,key_value,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), (5, 5), 5),
        (((2, 2), (3, 3), (4, 4), (5, 5)), (4, 10), 4),
        (((5, 5),), (1, 1), 2),
        ((), (1, 1), 1),
    ],
)
def test_put(elements, key_value, expected):
    avl_tree = dummy_avl_tree(elements)
    put(avl_tree, *key_value)
    assert avl_tree.size == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 4, (4, 3)),
        (((2, 2), (3, 3), (4, 4), (5, 5)), 2, (2, 3)),
        (((5, 5),), 5, (5, 0)),
    ],
)
def test_remove(elements, key, expected):
    avl_tree = dummy_avl_tree(elements)
    assert remove(avl_tree, key), avl_tree.size == expected


@pytest.mark.parametrize(
    "elements,key",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 5),
        (((1, 1), (2, 2), (3, 3), (4, 4)), 7),
        ((), 1),
    ],
)
def test_error_get(elements, key):
    avl_tree = dummy_avl_tree(elements)
    with pytest.raises(ValueError):
        get(avl_tree, key)


def test_error_get_minimum():
    avl_tree = create_tree_map()
    with pytest.raises(ValueError):
        get_minimum(avl_tree)


@pytest.mark.parametrize(
    "elements,key",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 5),
        (((2, 2), (3, 3), (4, 4), (5, 5)), 6),
        (((5, 5),), 6),
    ],
)
def test_error_get_lower_bound(elements, key):
    avl_tree = dummy_avl_tree(elements)
    with pytest.raises(ValueError):
        get_lower_bound(avl_tree, key)


@pytest.mark.parametrize(
    "elements,key",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 4),
        (((2, 2), (3, 3), (4, 4), (5, 5)), 5),
        (((5, 5),), 6),
    ],
)
def test_error_get_upper_bound(elements, key):
    avl_tree = dummy_avl_tree(elements)
    with pytest.raises(ValueError):
        get_upper_bound(avl_tree, key)


@pytest.mark.parametrize(
    "elements,key",
    [
        (((1, 1), (2, 2), (3, 3), (4, 4)), 100),
        (((2, 2), (3, 3), (4, 4), (5, 5)), 1),
        (((5, 5),), 6),
    ],
)
def test_error_remove(elements, key):
    avl_tree = dummy_avl_tree(elements)
    with pytest.raises(ValueError):
        remove(avl_tree, key)
