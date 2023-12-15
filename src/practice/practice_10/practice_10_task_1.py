from src.practice.practice_10.parser_module import *


def main():
    user_input = input(
        "Enter mathematical expression with spaces. Example '( 1 + 2 ) * 8': "
    )
    tokens = user_input.split()
    try:
        if len(user_input) == 0:
            raise ValueError("Entered empty line")
        pretty_print(parse(tokens))
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
