from src.test.test_3.task_1 import *
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "size",
    [1, 2, 5, 10, 13],
)
def test_vertical_symmetry(size):
    sprite = vertical_symmetry(size)
    for column in range(size):
        for row in range(ceil(size / 2)):
            assert sprite[row][column] == sprite[size - row - 1][column]


@pytest.mark.parametrize(
    "size",
    [1, 2, 5, 10, 19],
)
def test_horizontal_symmetry(size):
    sprite = horizontal_symmetry(size)
    for column in range(ceil(size / 2)):
        for row in range(size):
            assert sprite[row][column] == sprite[row][size - column - 1]


@pytest.mark.parametrize(
    "size",
    [1, 2, 5, 10, 17],
)
def test_complete_symmetry(size):
    sprite = complete_symmetry(size)
    for column in range(ceil(size / 2)):
        for row in range(ceil(size / 2)):
            assert (
                sprite[row][column]
                == sprite[row][size - column - 1]
                == sprite[size - row - 1][column]
                == sprite[size - row - 1][size - column - 1]
            )


@pytest.mark.parametrize(
    "sprite,expected",
    [
        (
            [
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
            ],
            "░░▓▓▓\n" "▓░▓░░\n" "▓▓▓░░\n" "▓░▓░░\n" "░░▓▓▓\n",
        ),
        (
            [[0, 0, 0], [1, 0, 1], [1, 1, 1]],
            "░▓▓\n" "░░▓\n" "░▓▓\n",
        ),
        (
            [[0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 1]],
            "░░░░\n" "▓░░▓\n" "▓▓▓▓\n" "▓░░▓\n",
        ),
    ],
)
def test_display(monkeypatch, sprite, expected):
    monkeypatch.setattr("builtins.input", lambda _: "")
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    display(sprite)
    output = fake_output.getvalue()
    assert output.split() == expected.split()


@pytest.mark.parametrize(
    "size",
    [0, -1, "size", "abbb", -12],
)
def test_main_scenario(monkeypatch, size):
    with pytest.raises(ValueError):
        monkeypatch.setattr("builtins.input", lambda _: size)
        fake_output = StringIO()
        monkeypatch.setattr("sys.stdout", fake_output)
        main()


@pytest.mark.parametrize(
    "user_input",
    [
        (["5", "", "a"]),
        (["7", "", "", "4"]),
        (["2", "b"]),
    ],
)
def test_main_scenario(monkeypatch, user_input):
    def check_symmetry(sprite: list[str]) -> bool:
        size = len(sprite)
        array_horizontal = []
        array_vertical = []

        for column in range(ceil(size / 2)):
            for row in range(size):
                array_vertical.append(
                    sprite[row][column] == sprite[size - row - 1][column]
                )
                array_horizontal.append(
                    sprite[row][column] == sprite[row][size - column - 1]
                )

        return all(array_vertical) or all(array_horizontal)

    number_of_inputs = len(user_input) - 1
    size = int(user_input[0])
    monkeypatch.setattr("builtins.input", lambda _: user_input.pop(0))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue().split("\n")

    for i in range(number_of_inputs):
        assert check_symmetry(output[i * size : (i + 1) * size])
