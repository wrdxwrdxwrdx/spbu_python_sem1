from src.practice.practice_7.TreeMap import *
import pytest


def dummy_bst(elements: tuple):
    map = create_tree_map()
    for i in elements:
        put(map, i[0], i[1])
    return map


def test_create_tree_map():
    map = create_tree_map()
    assert isinstance(map, TreeMap)


@pytest.mark.parametrize(
    "elements",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6))),
        (()),
    ],
)
def test_delete_tree_map(elements):
    map = dummy_bst(elements)
    delete_tree_map(map)
    assert map.root is None


@pytest.mark.parametrize(
    "elements,order,expected",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6)), "inorder", [1, 3, 6, 8]),
        (((8, 8), (3, 3), (1, 1), (6, 6)), "Inorder", [1, 3, 6, 8]),
        (((8, 8), (3, 3), (1, 1), (6, 6)), "postorder", [1, 6, 3, 8]),
        (((8, 8), (3, 3), (1, 1), (6, 6)), "preorder", [8, 3, 1, 6]),
        ((), "postorder", []),
    ],
)
def test_traverse(elements, order, expected):
    map = dummy_bst(elements)
    assert traverse(map, order) == expected


@pytest.mark.parametrize(
    "elements,put_element,expected",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6)), (1, 12), [12, 3, 6, 8]),
        (((8, 8), (3, 3), (1, 1), (6, 6)), (10, 10), [1, 3, 6, 8, 10]),
        ((), (1, 1), [1]),
    ],
)
def test_put(elements, put_element, expected):
    map = dummy_bst(elements)
    put(map, *put_element)
    assert traverse(map, "inorder") == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6)), 1, 1),
        (((8, 8), (3, 3), (1, 1), (6, 6)), 6, 6),
    ],
)
def test_get(elements, key, expected):
    map = dummy_bst(elements)
    assert get(map, key) == expected


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6)), 1, True),
        (((8, 8), (3, 3), (1, 1), (6, 6)), 10, False),
    ],
)
def test_has_element(elements, key, expected):
    map = dummy_bst(elements)
    assert has_key(map, key) == expected


@pytest.mark.parametrize(
    "elements,key,expected_value,expected_order",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6)), 1, 1, [3, 6, 8]),
        (
            (
                (8, 8),
                (3, 3),
                (1, 1),
                (6, 6),
                (4, 4),
                (7, 7),
                (10, 10),
                (14, 14),
                (13, 13),
            ),
            6,
            6,
            [1, 3, 4, 7, 8, 10, 13, 14],
        ),
    ],
)
def test_remove(elements, key, expected_value, expected_order):
    map = dummy_bst(elements)
    remove_value = remove(map, key)
    assert remove_value == expected_value and traverse(map, "inorder") == expected_order


@pytest.mark.parametrize(
    "elements,key",
    [
        ((()), 1),
        (((8, 8), (3, 3), (1, 1), (6, 6)), 12),
    ],
)
def test_error_get(elements, key):
    map = dummy_bst(elements)
    with pytest.raises(ValueError):
        get(map, key)


@pytest.mark.parametrize(
    "elements,key",
    [
        ((()), 1),
        (((8, 8), (3, 3), (1, 1), (6, 6)), 12),
    ],
)
def test_error_remove(elements, key):
    map = dummy_bst(elements)
    with pytest.raises(ValueError):
        remove(map, key)


@pytest.mark.parametrize(
    "elements,order",
    [
        (((8, 8), (3, 3), (1, 1), (6, 6)), "postorderrr"),
        (((8, 8), (3, 3), (1, 1), (6, 6)), "order"),
    ],
)
def test_error_traverse(elements, order):
    map = dummy_bst(elements)
    with pytest.raises(ValueError):
        traverse(map, order)
