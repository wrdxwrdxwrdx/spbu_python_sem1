def compare_numbers(number, attempt):
    bull = 0  # точные места
    cow = 0  # не точные места

    for i in range(len(number)):
        if attempt[i] == number[i]:
            bull += 1
        elif attempt[i] in number:
            cow += 1

    return (cow, bull)


def input_names():
    player_1_name = input('Введите имя первого игрока: ')
    player_2_name = input('Введите имя второго игрока: ')
    return player_1_name, player_2_name


def skip_line(line_number):
    for _ in range(line_number):
        print('\n')


def player_move(player_name, number):
    skip_line(20)

    bull = 0
    cow = 0
    points = 1

    while bull != 4:
        attempt = input(
            f'{points}) {player_name} пожалуйста введите 4 значное число без повторений цифр: ')
        if not is_number_available(attempt):
            print('Неверное число')
            continue
        points += 1

        cow, bull = compare_numbers(number, attempt)
        print(f"{cow} коровы, {bull} быков\n")
    points -= 1
    print(f'{player_name} угадал число за {points} ходов')
    return points


def is_number_available(number):
    if not (len(number) == 4 and len(set(number)) == 4):
        return False
    return True


if __name__ == '__main__':
    print(
        'Игрок 1 вводит число, после этого игрок 2 его угадывает. Потом наоборот. Побеждает тот, кто угадал число быстрее\n')
    player_1_name, player_2_name = input_names()

    player_1_number = input(f'\n{player_1_name} пожалуйста введите 4 значное число без повторений цифр: ')
    if not is_number_available(player_1_number):
        while not (is_number_available(player_1_number)):
            print('Неверное число')
            player_1_number = input(f'\n{player_1_name} пожалуйста введите 4 значное число без повторений цифр: ')

    player_2_points = player_move(player_2_name, player_1_number)

    player_2_number = input(f'\n{player_2_name} пожалуйста введите 4 значное число без повторений цифр: ')
    if not is_number_available(player_2_number):
        while not (is_number_available(player_2_number)):
            print('Неверное число')
            player_2_number = input(f'\n{player_2_name} пожалуйста введите 4 значное число без повторений цифр: ')

    player_1_points = player_move(player_1_name, player_2_number)

    if player_1_points < player_2_points:
        print(f'\n{player_1_name} победил. Он угадал число на {player_2_points - player_1_points} ходов быстрее')
    elif player_2_points < player_1_points:
        print(f'\n{player_2_name} победил. Он угадал число на {player_1_points - player_2_points} ходов быстрее')
    else:
        print('\nНичья')
