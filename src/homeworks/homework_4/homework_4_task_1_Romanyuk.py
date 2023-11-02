from math import *


def normalize_binary(number, bits):
    return [number[0]] * (bits - len(number)) + number


def get_size_bytes(number):
    return ceil(len(number) / 8)


def binary_addition(num_1, num_2):
    extra_number = 0
    answer = []

    for i in range(len(num_1) - 1, -1, -1):
        sum_digit = extra_number + num_1[i] + num_2[i]

        if sum_digit > 1:
            extra_number = 1
        else:
            extra_number = 0
        answer.insert(0, sum_digit % 2)

    if len(answer) > len(num_1):
        return normalize_binary(answer[1:], len(answer[1:]))
    return normalize_binary(answer, len(answer))


def denary_to_binary(number):
    is_minus = number < 0
    answer = []
    number = abs(number)

    while number >= 1:
        answer.insert(0, number % 2)
        number //= 2

    binary_one = normalize_binary([0, 1], len(answer))

    if is_minus:
        return [1] + binary_addition(inverse_number(answer), binary_one)
    return [0] + answer


def binary_to_denary(number):
    answer = 0
    is_minus = number.pop(0)
    if is_minus:
        number = binary_addition(
            inverse_number(number), normalize_binary([0, 1], len(number))
        )[::-1]
    else:
        number = number[::-1]
    for i in range(len(number)):
        answer += number[i] * (2**i)
    return (-1) ** is_minus * answer


def inverse_number(number):
    return list(map(lambda x: int(not x), number))


def binary_subtraction(num_1, num_2):
    num_2 = binary_addition(inverse_number(num_2), normalize_binary([0, 1], len(num_2)))
    bytes = max(get_size_bytes(num_1), get_size_bytes(num_2))
    return binary_addition(
        normalize_binary(num_1, bytes * 8), normalize_binary(num_2, bytes * 8)
    )


def arr_to_str(arr):
    return "".join(map(str, arr))


def main():
    num_1 = int(input("Первое число: "))
    num_2 = int(input("Второе число: "))
    num_1_bin, num_2_bin = denary_to_binary(num_1), denary_to_binary(num_2)

    bytes = max(get_size_bytes(num_1_bin), get_size_bytes(num_2_bin)) + 1

    num_1_bin = normalize_binary(num_1_bin, bytes * 8)
    num_2_bin = normalize_binary(num_2_bin, bytes * 8)

    print(f"{num_1} в Двоичной системе исчисления: {arr_to_str(num_1_bin)}")
    print(f"{num_2} в Двоичной системе исчисления: {arr_to_str(num_2_bin)}")
    print(
        f"{num_1} + {num_2} в Двоичной системе исчисления: {arr_to_str(binary_addition(num_1_bin, num_2_bin))}"
    )
    print(
        f"{num_1} + {num_2} в Десятичной системе исчисления: {binary_to_denary(binary_addition(num_1_bin, num_2_bin))}"
    )
    print(
        f"{num_1} - {num_2} в Двоичной системе исчисления: {arr_to_str(binary_subtraction(num_1_bin, num_2_bin))}"
    )
    print(
        f"{num_1} - {num_2} в Десятичной системе исчисления: {binary_to_denary(binary_subtraction(num_1_bin, num_2_bin))}"
    )


if __name__ == "__main__":
    main()
