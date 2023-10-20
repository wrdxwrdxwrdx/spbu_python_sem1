def is_float_number(num):
    try:
        float(num)
    except ValueError:
        return False
    return True


def linear_solver(k, b):
    return [-b / k]


def quadratic_solver(a, b, c):
    dis = b**2 - 4 * a * c

    if dis < 0:
        raise ValueError("Дискриминант меньше 0")
    elif dis == 0:
        return [-b / (2 * a)]
    else:
        x1 = (-b + dis**0.5) / (2 * a)
        x2 = (-b - dis**0.5) / (2 * a)
        return list(sorted([x1, x2]))


def solve(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            print("x любое число")
            return []
        else:
            raise ValueError("нет решений")

    elif a == 0:
        return linear_solver(b, c)
    else:
        return quadratic_solver(a, b, c)


def string_to_float(line):
    if all(is_float_number(i) for i in line.split()):
        return list(map(float, line.split()))
    else:
        raise ValueError("Один из коэффициентов не число")


def check_user_input(line, number_of_elements):
    if len(line.split()) == number_of_elements:
        return True
    return False


def show_answer(arr):
    print(" ".join(map(str, arr)))


def main():
    user_input = input("Введите a, b, c для уравнения ax^2 + bx + c = 0: ")

    if check_user_input(user_input, 3):
        answer_array = solve(*string_to_float(user_input))
        show_answer(answer_array)
    else:
        raise ValueError("Введено не 3 параметра")


if __name__ == "__main__":
    main()
