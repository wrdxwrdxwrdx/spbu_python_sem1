def denary_to_binary(number):
    answer = []

    is_minus = number < 0
    number = abs(number)

    while number > 0:
        answer.append(number % 2)
        number //= 2

    answer = answer[::-1]
    answer.insert(0, 0)

    if is_minus:
        answer = list(map(lambda a: 0 if a else 1, answer))
        answer = binary_addition(answer, [0, 1])
    return answer


def normalize_binary(a, b):
    if len(b) < len(a):
        b = [b[0] for i in range(len(a) - len(b) + 2)] + b[1:]
        a = [a[0]] + a
    else:
        a = [a[0] for i in range(len(b) - len(a) + 2)] + a[1:]
        b = [b[0]] + b
    return a, b


def binary_addition(q, w):
    a, b = normalize_binary(q, w)

    for i in range(len(a)):
        b[i] += a[i]

    for i in range(len(b) - 1, -1, -1):
        if b[i] >= 2:
            if i != 0:
                b[i - 1] += b[i] // 2
                b[i] = b[i] % 2
            else:
                b[i] = 0
    return b


def binary_subtraction(a, b):
    return binary_addition(a, invert_number(b))


def arr_to_str(arr):
    return "".join(map(str, arr))


def invert_number(number):
    if number[0] == 0:
        answer = list(map(lambda a: 0 if a else 1, number))
        answer = binary_addition(answer, [0, 1])
    else:
        answer = list(map(lambda a: 0 if a else 1, number))
        answer = binary_addition(answer, [0, 1])
    return answer


def binary_to_denary(number):
    answer = 0
    minus = number.pop(0)
    if minus:
        number = invert_number(number)[::-1]
    else:
        number = number[::-1]

    for i in range(len(number)):
        answer += number[i] * 2**i

    if minus:
        return -answer
    return answer


def main(num_1, num_2):
    num_1_bin, num_2_bin = denary_to_binary(num_1), denary_to_binary(num_2)
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
    num_1 = int(input("Первое число: "))
    num_2 = int(input("Второе число: "))

    main(num_1, num_2)
