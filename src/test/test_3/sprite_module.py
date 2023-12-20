import random
from math import ceil

BLACK_SQUARE = "▓"
WHITE_SQUARE = "░"


def vertical_symmetry(size: int) -> list[list[int]]:
    sprite = [[0 for _ in range(size)] for _ in range(size)]
    for column in range(size):
        for row in range(ceil(size / 2)):
            if random.randint(0, 1):
                sprite[row][column] = 1
                sprite[size - row - 1][column] = 1
    return sprite


def horizontal_symmetry(size: int) -> list[list[int]]:
    sprite = [[0 for _ in range(size)] for _ in range(size)]
    for column in range(ceil(size / 2)):
        for row in range(size):
            if random.randint(0, 1):
                sprite[row][column] = 1
                sprite[row][size - column - 1] = 1
    return sprite


def complete_symmetry(size: int) -> list[list[int]]:
    sprite = [[0 for _ in range(size)] for _ in range(size)]
    for column in range(ceil(size / 2)):
        for row in range(ceil(size / 2)):
            if random.randint(0, 1):
                sprite[row][column] = 1
                sprite[row][size - column - 1] = 1
                sprite[size - row - 1][column] = 1
                sprite[size - row - 1][size - column - 1] = 1
    return sprite


def display(sprite: list[list[int]]):
    size = len(sprite)

    for column in range(size):
        line = ""
        for row in range(size):
            if sprite[row][column]:
                line += BLACK_SQUARE
            else:
                line += WHITE_SQUARE
        print(line)
