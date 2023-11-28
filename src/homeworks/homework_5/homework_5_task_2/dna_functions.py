import string


def is_valid_dna_code(dna_code: str) -> None:
    if not all(
        map(lambda x: x in string.digits or x in string.ascii_letters, dna_code)
    ):
        raise ValueError("Код днк должен содержать только буквы латиницы")

    if not dna_code[-1].isdigit():
        raise ValueError("Код днк не должен заканчиваться буквой")

    if dna_code[0].isdigit():
        raise ValueError("Код днк не должен начинаться с числа")

    chars = (
        "".join(list(map(lambda char: " " if char.isdigit() else char, dna_code)))
    ).split()
    numbers = (
        "".join(list(map(lambda char: " " if char.isalpha() else char, dna_code)))
    ).split()

    if "0" in numbers:
        raise ValueError("Код днк не должен содержать 0")

    output = list(map(lambda char: len(char) == 1, chars))

    if not all(output):
        raise ValueError("Код днк не должен содержать две буквы подряд")


def is_valid_dna(dna: str) -> None:
    if not all(map(lambda x: x in string.digits or x in string.ascii_letters, dna)):
        raise ValueError("Код днк должен содержать только буквы латиницы")

    numbers = (
        "".join(list(map(lambda char: " " if char.isalpha() else char, dna)))
    ).split()

    if len(numbers) >= 1:
        raise ValueError("В днк не должно быть цифр")


def encode(dna: str) -> str:
    is_valid_dna(dna)

    output = ""

    start_pointer = 0
    end_pointer = 0

    while end_pointer < len(dna):
        while end_pointer < len(dna) and dna[start_pointer] == dna[end_pointer]:
            end_pointer += 1
        output += f"{dna[start_pointer]}{end_pointer-start_pointer}"
        start_pointer = end_pointer

    return output


def decode(dna_code: str) -> str:
    is_valid_dna_code(dna_code)

    chars = (
        "".join(list(map(lambda char: " " if char.isdigit() else char, dna_code)))
    ).split()

    numbers = (
        "".join(list(map(lambda char: " " if char.isalpha() else char, dna_code)))
    ).split()

    output = "".join(
        list(map(lambda index: chars[index] * int(numbers[index]), range(len(chars))))
    )

    return output
