from dataclasses import dataclass, field
from typing import TypeVar

State = TypeVar("State")


@dataclass
class FSMachine:
    table: dict = field(default_factory=dict)
    functions: list = field(default_factory=list)
    start_state: State = 0
    quit_states: list = field(default_factory=list)


def create_fs_machine(
    table: dict, functions: list, start_state: State, quit_states: list
) -> FSMachine:
    """create fsm with table, start_state, quit_states and functions\n
    functions: [f1, f2, f3 ...]\n
    table:\n
    s | f1  | f2 | f3 | ... \n
    0 |None| 1  | 2 | ... \n
    1 |None| 2  | 3 | ... \n
    ...\n
    {0 : (None, 1, 2, ...),\n
    1 : (None, 2, 3, ...), }\n
    The key is the current state. The value is all the states that can be
    accessed from it, depending on the value of the function. "None" indicates
    the impossibility of such a transition from state.
    """

    fsm = FSMachine()

    fsm.table = table
    fsm.functions = functions
    fsm.quit_states = quit_states
    fsm.start_state = start_state
    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    """check is string valid in fsm language"""
    current_state = fsm.start_state
    index = 0
    while index != len(string):
        for next_state_index, func in enumerate(fsm.functions):
            if func(string[index]):
                current_state = fsm.table[current_state][next_state_index]
                if current_state is None:
                    return False
                index += 1
                break
        else:
            return False
    return current_state in fsm.quit_states
