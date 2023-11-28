from math import *


def normalize_binary(number, bits):
    return [number[0]] * (bits - len(number)) + number


def get_size_bytes(number):
    return ceil(len(number) / 8)


def binary_addition(num_1, num_2):
    extra_number = 0
    output = []

    for i in range(1, len(num_1) + 1):
        sum_digit = extra_number + num_1[-i] + num_2[-i]

        if sum_digit > 1:
            extra_number = 1
        else:
            extra_number = 0
        output.append(sum_digit % 2)
    output = output[::-1]
    if len(output) > len(num_1):
        return normalize_binary(output[1:], len(output[1:]))
    return normalize_binary(output, len(output))


def denary_to_binary(number):
    output = []
    abs_number = abs(number)

    while abs_number >= 1:
        output.append(abs_number % 2)
        abs_number //= 2
    output = output[::-1]
    binary_one = normalize_binary([0, 1], len(output))
    if number < 0:
        return [1] + binary_addition(inverse_number(output), binary_one)
    return [0] + output


def binary_to_denary(number):
    output = 0
    for i in range(1, len(number) + 1):
        output += number[-i] * 2 ** (i - 1)

        if i == len(number):
            output -= number[-i] * 2**i
    return output


def inverse_number(number):
    return list(map(lambda a: 0 if a else 1, number))


def binary_subtraction(num_1, num_2):
    output = binary_addition(
        inverse_number(num_2), normalize_binary([0, 1], len(num_2))
    )
    bytes = max(get_size_bytes(num_1), get_size_bytes(output))
    return binary_addition(
        normalize_binary(num_1, bytes * 8), normalize_binary(output, bytes * 8)
    )


def main():
    def arr_to_str(arr):
        return "".join(map(str, arr))

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
