INPUT_TEXT = "Введите строку для кодировки в UTF-16:\n"


def get_unicode(char: str) -> str:
    unicode = hex(ord(char))[2:].upper()
    return f"U+{(unicode.rjust( 4, '0'))}"


def get_unicode_binary(char: str) -> str:
    binary_unicode = bin(ord(char))[2:]
    answer = binary_unicode.rjust(32, "0")
    return " ".join([answer[i : i + 8] for i in range(0, 32, 8)])


def main():
    user_input = input(INPUT_TEXT)

    for char in user_input:
        unicode = get_unicode(char)
        unicode_binary = get_unicode_binary(char)
        print("{}   {}  {}".format(char, unicode, unicode_binary))


if __name__ == "__main__":
    main()
