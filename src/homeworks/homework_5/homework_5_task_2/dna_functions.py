import re


def is_valid_dna_code(dna_code: str) -> bool:
    if re.search("[а-яА-я]", dna_code):
        raise ValueError("Код днк должен содержать только буквы латиницы")

    if not dna_code[-1].isdigit():
        raise ValueError("Код днк не должен заканчиваться буквой")

    if dna_code[0].isdigit():
        raise ValueError("Код днк не должен начинаться с числа")

    output = []

    def digit_check(array: list, match: re.Match) -> str:
        array.append(dna_code[match.span()[0] - 1].isdigit())
        return match[0]

    re.sub("[a-zA-z]", lambda x: digit_check(output, x), dna_code)

    def char_check(array: list, match: re.Match) -> str:
        if match.group() == "0":
            raise ValueError("Код днк не должен содержать 0")
        array.append(dna_code[match.span()[0] - 1].isalpha())
        return match[0]

    re.sub("[0-9]+", lambda x: char_check(output, x), dna_code)

    return all(output)


def is_valid_dna(dna: str) -> bool:
    if re.search("[а-яА-я]", dna):
        raise ValueError("Днк должен содержать только буквы латиницы")

    return bool(re.match("^[a-zA-z]+$", dna))


def encode(dna: str) -> str:
    if not is_valid_dna(dna):
        raise ValueError("В днк не должно быть цифр")

    output = re.sub(r"(\w)\1*", lambda x: f"{x[1]}{len(x[0])}", dna)

    return output


def decode(dna_code: str) -> str:
    pattern = "[A-Za-z]+[0-9]*"

    if not is_valid_dna_code(dna_code):
        raise ValueError("Код днк не должен содержать две буквы подряд")

    return re.sub(pattern, lambda x: f"{x[0][0]*int(x[0][1:])}", dna_code)
