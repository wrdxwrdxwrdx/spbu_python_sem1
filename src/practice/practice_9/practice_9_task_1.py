from src.practice.practice_9.fsm_module import *
from string import digits


def create_fsm_ab() -> FSMachine:
    name_ab = "(a|b)*abb"
    rules_ab = ["a", "b"]
    table_ab = {
        0: (1, 0),
        1: (1, 2),
        2: (1, 3),
        3: (1, 0),
    }
    start_state_ab = 0
    quit_states_ab = [3]

    fsm_ab = create_fs_machine(
        name_ab, table_ab, rules_ab, start_state_ab, quit_states_ab
    )
    return fsm_ab


def create_fsm_number() -> FSMachine:
    name_number = "digit+(.digit+)?(E(+|-)?digit+)?"
    rules_number = [digits, ".", "E", "-+"]
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

    fsm_number = create_fs_machine(
        name_number, table_number, rules_number, start_state_number, quit_states_number
    )
    return fsm_number


def main():
    fsm_array = [create_fsm_ab(), create_fsm_number()]

    user_word = input("Enter word: ")
    for fsm in fsm_array:
        if validate_string(fsm, user_word):
            print(f"{user_word} is {fsm.name} language")
            break
    else:
        print(f"{user_word} is not any language")


if __name__ == "__main__":
    main()
