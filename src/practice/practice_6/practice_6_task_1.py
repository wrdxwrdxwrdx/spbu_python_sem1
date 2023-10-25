INPUT_TEXT = "Введите a, b, c для уравнения ax^2 + bx + c = 0 или 0, k, b для уравнения kx + b = 0: "
BAD_INPUT = "Введено не 3 параметра"


def is_float_number(num):
    try:
        float(num)
    except ValueError:
        return False
    return True


def linear_solver(k, b):
    if k == 0:
        raise ValueError("Нет решений, нельзя делить на 0")
    return (-b / k,)


def quadratic_solver(a, b, c):
    dis = b**2 - 4 * a * c

    if dis < 0:
        raise ValueError("Дискриминант меньше 0")
    elif dis == 0:
        return (-b / (2 * a),)
    else:
        x1 = (-b + dis**0.5) / (2 * a)
        x2 = (-b - dis**0.5) / (2 * a)
        return (x1, x2)


def solve(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            raise ValueError("все коэффициенты равны 0, x любое число")
        else:
            raise ValueError("нет решений")

    elif a == 0:
        return linear_solver(b, c)
    else:
        return quadratic_solver(a, b, c)


def string_to_float(line):
    if all(is_float_number(i) for i in line.split()):
        return tuple(map(float, line.split()))
    else:
        raise ValueError("Один из коэффициентов не число")


def check_user_input(line, number_of_elements):
    return len(line.split()) == number_of_elements


def main():
    user_input = input(INPUT_TEXT)

    if check_user_input(user_input, 3):
        answer_array = solve(*string_to_float(user_input))
        print(*answer_array, sep=" ")
    else:
        raise ValueError(BAD_INPUT)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
