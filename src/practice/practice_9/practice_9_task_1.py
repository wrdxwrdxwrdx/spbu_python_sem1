from src.practice.practice_9.fsm_module import *
from string import digits


def main():
    functions_ab = [lambda x: x == "a", lambda x: x == "b"]
    table_ab = {
        0: (1, 0),
        1: (1, 2),
        2: (1, 3),
        3: (1, 0),
    }
    start_state_ab = 0
    quit_states_ab = [3]

    functions_number = [
        lambda x: x in digits,
        lambda x: x == ".",
        lambda x: x == "E",
        lambda x: x == "-" or x == "+",
    ]
    table_number = {
        0: (2, 3, None, 1),
        1: (2, 3, None, None),
        2: (2, 3, 5, None),
        3: (4, None, None, None),
        4: (4, None, 5, None),
        5: (7, None, None, 6),
        6: (7, None, None, None),
        7: (7, None, None, None),
    }
    start_state_number = 0
    quit_states_number = [2, 4, 7]

    fsm_ab = create_fs_machine(table_ab, functions_ab, start_state_ab, quit_states_ab)
    fsm_number = create_fs_machine(
        table_number, functions_number, start_state_number, quit_states_number
    )

    user_word = input("Enter word: ")
    if validate_string(fsm_ab, user_word):
        print(f"{user_word} is (a|b)*abb language")
    elif validate_string(fsm_number, user_word):
        print(f"{user_word} is digit+(.digit+)?(E(+|-)?digit+)? language")
    else:
        print(f"{user_word} is not any language")


if __name__ == "__main__":
    main()
