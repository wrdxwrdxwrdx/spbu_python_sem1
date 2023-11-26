from src.homeworks.homework_6.homework_6_task_2.homework_6_task_2 import *
import pytest


def dummy_avl_tree(elements: tuple) -> TreeMap:
    avl_tree = create_tree_map()
    for key_value in elements:
        put(avl_tree, *key_value)
    return avl_tree


def dummy_storage(elements: tuple) -> TreeMap:
    storage = create_tree_map()
    for address_index in elements:
        create_address(storage, *address_index)
    return storage


def test_static_mode():
    storage = create_tree_map()
    static_mode(storage, "streets_logs.txt", "streets_results.txt")
    is_output = True
    with open("streets_results.txt", "r") as result:
        with open("streets_answer.txt", "r") as answer:
            result_lines = result.readlines()
            answer_lines = answer.readlines()
            for i in range(len(result_lines)):
                if result_lines[i] != answer_lines[i]:
                    is_output = False
    assert is_output


@pytest.mark.parametrize(
    "storage_elements,address_1, address_2,expected",
    [
        (
            (
                ["Близкая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Близкая 12 3", 3],
            ),
            "Близкая 11 2",
            "Близкая 12 3",
            ["Близкая 11 2"],
        ),
        (
            (
                ["Апокалиптическая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Апокалиптическая 14 3", 3],
            ),
            "Аба 1 1",
            "Апокалиптическая 14 4",
            ["Апокалиптическая 11 2", "Апокалиптическая 14 3"],
        ),
        (
            (
                ["Апокалиптическая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Апокалиптическая 14 3", 3],
            ),
            "Близкая 11 2",
            "Близкая 12 3",
            [],
        ),
    ],
)
def test_list_command(storage_elements, address_1, address_2, expected):
    storage = dummy_storage(storage_elements)
    assert list_command(storage, address_1, address_2) == expected


@pytest.mark.parametrize(
    "storage_elements,street,expected",
    [
        (
            (
                ["Близкая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Близкая 12 3", 3],
            ),
            "Близкая",
            [
                (["Синяя", 10, 3], 2),
            ],
        ),
        (
            (
                ["Апокалиптическая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Апокалиптическая 14 3", 3],
            ),
            "Апокалиптическая",
            [
                (["Синяя", 10, 3], 2),
            ],
        ),
    ],
)
def test_delete_street(storage_elements, street, expected):
    storage = dummy_storage(storage_elements)
    delete_street(storage, street)
    assert sorted(traverse(storage)) == sorted(expected)


@pytest.mark.parametrize(
    "storage_elements,street,house,expected",
    [
        (
            (
                ["Близкая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Близкая 11 3", 3],
            ),
            "Близкая",
            "11",
            [
                (["Синяя", 10, 3], 2),
            ],
        ),
        (
            (
                ["Апокалиптическая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Апокалиптическая 11 3", 3],
            ),
            "Апокалиптическая",
            "11",
            [
                (["Синяя", 10, 3], 2),
            ],
        ),
    ],
)
def test_delete_house(storage_elements, street, house, expected):
    storage = dummy_storage(storage_elements)
    delete_house(storage, street, house)
    assert sorted(traverse(storage)) == sorted(expected)


@pytest.mark.parametrize(
    "storage_elements,address,expected",
    [
        (
            (
                ["Близкая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Близкая 11 3", 3],
            ),
            "Близкая 11 2",
            [
                (["Синяя", 10, 3], 2),
                (["Близкая", 11, 3], 3),
            ],
        ),
        (
            (
                ["Апокалиптическая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Апокалиптическая 11 3", 3],
            ),
            "Апокалиптическая 11 2",
            [
                (["Синяя", 10, 3], 2),
                (["Апокалиптическая", 11, 3], 3),
            ],
        ),
    ],
)
def test_delete_block(storage_elements, address, expected):
    storage = dummy_storage(storage_elements)
    delete_block(storage, address)
    assert sorted(traverse(storage)) == sorted(expected)


@pytest.mark.parametrize(
    "storage_elements,previous_street,new_street,expected",
    [
        (
            (
                ["Близкая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Близкая 11 3", 3],
            ),
            "Близкая",
            "Одуванчиков",
            [
                (["Одуванчиков", 11, 2], 1),
                (["Синяя", 10, 3], 2),
                (["Одуванчиков", 11, 3], 3),
            ],
        ),
        (
            (
                ["Апокалиптическая 11 2", 1],
                ["Синяя 10 3", 2],
                ["Апокалиптическая 11 3", 3],
            ),
            "Апокалиптическая",
            "Одуванчиков",
            [
                (["Одуванчиков", 11, 2], 1),
                (["Синяя", 10, 3], 2),
                (["Одуванчиков", 11, 3], 3),
            ],
        ),
    ],
)
def test_rename_street(storage_elements, previous_street, new_street, expected):
    storage = dummy_storage(storage_elements)
    rename_street(storage, previous_street, new_street)
    assert sorted(traverse(storage)) == sorted(expected)


@pytest.mark.parametrize(
    "address,index",
    [
        ("Близкая 11 2", 0),
        ("Близкая 11 3", 5),
        ("Близкая 1 4", 6),
        ("Синяя 9 1", 17),
        ("Синяя 10 3", 18),
    ],
)
def test_get_index(address, index):
    storage = create_tree_map()

    create_address(storage, address, index)
    assert get_index(storage, address) == index


@pytest.mark.parametrize(
    "address,index",
    [
        ("Близкая 11 2", 0),
        ("Близкая 11 3", 5),
        ("Близкая 1 4", 6),
        ("Синяя 9 1", 17),
        ("Синяя 10 3", 18),
    ],
)
def test_create_address(address, index):
    storage = create_tree_map()

    create_address(storage, address, index)
    assert (format_address(address), index) in traverse(storage)


@pytest.mark.parametrize(
    "address,expected",
    [
        ("street 1 2", ["street", 1, 2]),
        ("Близкая 11 2", ["Близкая", 11, 2]),
        ("Близкая 11 3", ["Близкая", 11, 3]),
        ("Близкая 1 4", ["Близкая", 1, 4]),
    ],
)
def test_format_address(address, expected):
    assert format_address(address) == expected


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
