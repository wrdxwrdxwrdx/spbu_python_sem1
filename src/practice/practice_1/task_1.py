def incomplete_quotient(a, b):
    answer = 0
    number = 0
    while number < a:
        number += b
        answer += 1
    if number > a:
        return answer - 1
    return answer


if __name__ == '__main__':
    input_info = input('Введите числа a и b через пробел: ')
    a, b = map(int, input_info.split())
    print(f'результат неполного частного от деления {a} на {b}: {incomplete_quotient(a, b)}')
