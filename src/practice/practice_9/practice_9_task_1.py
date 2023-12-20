from src.practice.practice_9.fsm_module import *
from string import digits


def create_fsm_ab() -> FSMachine:
    name_ab = "(a|b)*abb"
    table_ab = (
        {"a": 1, "b": 0},
        {"a": 1, "b": 2},
        {"a": 1, "b": 3},
        {"a": 1, "b": 0},
    )
    start_state_ab = 0
    quit_states_ab = [3]

    fsm_ab = create_fs_machine(name_ab, table_ab, start_state_ab, quit_states_ab)
    return fsm_ab


def create_fsm_number() -> FSMachine:
    name_number = "digit+(.digit+)?(E(+|-)?digit+)?"
    table_number = (
        {digits: 1, ".": 3, "-+": 1},
        {digits: 2, ".": 3},
        {digits: 2, ".": 3, "E": 5},
        {digits: 4},
        {digits: 4, "E": 5},
        {digits: 7, "-+": 6},
        {digits: 7},
        {digits: 7},
    )
    start_state_number = 0
    quit_states_number = [2, 4, 7]

    fsm_number = create_fs_machine(
        name_number, table_number, start_state_number, quit_states_number
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
