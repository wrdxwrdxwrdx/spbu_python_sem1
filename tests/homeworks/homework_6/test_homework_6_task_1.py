import random

from src.homeworks.homework_6.AVL_Tree import *
import pytest


def traverse(tree_map: TreeMap) -> list[(Key, Value)]:
    def traverse_node(root: TreeNode) -> list[(Key, Value)]:
        if root is None:
            return []
        key_arr = [(root.key, root.value)]
        key_arr += traverse_node(root.left) + traverse_node(root.right)
        return key_arr

    return traverse_node(tree_map.root)


def dummy_avl_tree(elements: tuple, to_balance=True) -> TreeMap:
    avl_tree = create_tree_map()
    for key_value in elements:
        put(avl_tree, *key_value, to_balance)
    return avl_tree


@pytest.mark.parametrize(
    "elements,expected_elements",
    [
        (
            ((0, 0), (-5, -5), (5, 5), (10, 10), (15, 15), (7, 7), (2, 2)),
            ((5, 5), (0, 0), (10, 10), (-5, -5), (2, 2), (7, 7), (15, 15)),
        ),
        (
            ((5, 5), (0, 0), (13, 13), (10, 10), (15, 15), (25, 25), (7, 7)),
            ((13, 13), (5, 5), (15, 15), (0, 0), (10, 10), (25, 25), (7, 7)),
        ),
    ],
)
def test_left_rotate(elements, expected_elements):
    avl_tree = dummy_avl_tree(elements, to_balance=False)
    expected_avl_tree = dummy_avl_tree(expected_elements, to_balance=False)
    avl_tree.root = left_rotate(avl_tree.root)

    assert traverse(avl_tree) == traverse(expected_avl_tree)


@pytest.mark.parametrize(
    "elements,expected_elements",
    [
        (
            ((0, 0), (-5, -5), (5, 5), (-10, -10), (-15, -15), (-7, -7), (-2, -2)),
            ((-5, -5), (-10, -10), (0, 0), (-15, -15), (-7, -7), (-2, -2), (5, 5)),
        ),
        (
            (
                (-5, -5),
                (0, 0),
                (-13, -13),
                (-10, -10),
                (-15, -15),
                (-25, -25),
                (-7, -7),
            ),
            (
                (-13, -13),
                (-15, -15),
                (-5, -5),
                (-25, -25),
                (-10, -10),
                (0, 0),
                (-7, -7),
            ),
        ),
    ],
)
def test_right_rotate(elements, expected_elements):
    avl_tree = dummy_avl_tree(elements, to_balance=False)
    expected_avl_tree = dummy_avl_tree(expected_elements, to_balance=False)
    avl_tree.root = right_rotate(avl_tree.root)

    assert traverse(avl_tree) == traverse(expected_avl_tree)


@pytest.mark.parametrize(
    "size",
    [2, 4, 6, 9, 12, 15, 20, 50],
)
def test_balance_tree(size):
    avl_tree = create_tree_map()
    for _ in range(size):
        random_value = random.randint(1, 100)
        put(avl_tree, random_value, random_value)
        assert abs(get_balance_factor(avl_tree.root)) < 2


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
