from dataclasses import dataclass, field


@dataclass
class FSMachine:
    name: str
    table: dict
    rules: list
    start_state: int
    quit_states: list


def create_fs_machine(
    name: str, table: dict, rules: list, start_state: int, quit_states: list
) -> FSMachine:
    """create fsm with table, start_state, quit_states and functions\n
    functions: ["a", "bc", "d" ...]\n
    table:\n
    s |  a | bc | d | ... \n
    0 |None| 1  | 2 | ... \n
    1 |None| 2  | 3 | ... \n
    ...\n
    {0 : (None, 1, 2, ...),\n
    1 : (None, 2, 3, ...), }\n
    The key is the current state. The value is all the states that can be
    accessed from it, depending on the value of the function. "None" indicates
    the impossibility of such a transition from state.
    """

    fsm = FSMachine(name, table, rules, start_state, quit_states)

    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    """check is string valid in fsm language"""
    current_state = fsm.start_state
    for index in range(len(string)):
        for next_state_index, rule in enumerate(fsm.rules):
            if string[index] in rule:
                current_state = fsm.table[current_state][next_state_index]
                if current_state is None:
                    return False
                break
        else:
            return False
    return current_state in fsm.quit_states
