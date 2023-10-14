import random


def compare_numbers(number, attempt):
    bull = 0  # точные места
    cow = 0  # не точные места

    for i in range(len(number)):
        if attempt[i] == number[i]:
            bull += 1
        elif attempt[i] in number:
            cow += 1

    return (cow, bull)


def player_move(number):
    bull = 0
    cow = 0
    moves = 1

    while bull != 4:
        attempt = input(
            f"{moves}) пожалуйста введите 4 значное число без повторений цифр: "
        )
        if not is_number_available(attempt):
            print("Неверное число")
            continue
        moves += 1

        cow, bull = compare_numbers(number, attempt)
        print(f"{cow} коровы, {bull} быков\n")
    moves -= 1
    print(f"Вы угадали число за {moves} ходов")
    return moves


def is_number_available(number):
    return len(number) == 4 and len(set(number)) == 4 and number[0] != "0"


def generate_number(number_length):
    number_list = list(range(10))
    while number_list[0] == 0:
        random.shuffle(number_list)
    return "".join(map(str, number_list[:number_length]))


def main():
    number = generate_number(4)

    while not (is_number_available(number)):
        print("Неверное число")
        player_number = input(
            f"\nпожалуйста введите 4 значное число без повторений цифр: "
        )

    player_points = player_move(number)


if __name__ == "__main__":
    main()
