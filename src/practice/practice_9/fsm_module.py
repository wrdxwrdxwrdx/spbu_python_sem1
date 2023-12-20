from dataclasses import dataclass


@dataclass
class FSMachine:
    name: str
    table: tuple[dict[str, int]]
    start_state: int
    quit_states: list


def create_fs_machine(
    name: str, table: tuple[dict[str, int]], start_state: int, quit_states: list
) -> FSMachine:
    """create fsm with table, start_state, quit_states and functions\n
    table:\n
    [\n
    {"a" : (None, 1, 2, ...), "bc" : (None, 2, 3, ...), },\n
    {"d" : (5, 1, None, ...), "123" : (2, 4, 3, ...), },\n
    ...\n
    ]
    """

    fsm = FSMachine(name, table, start_state, quit_states)

    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    """check is string valid in fsm language"""
    current_state = fsm.start_state
    for token in string:
        state_rules = fsm.table[current_state]
        for rule in state_rules.keys():
            if token in rule:
                current_state = state_rules[rule]
                if current_state is None:
                    return False
                break
        else:
            return False
    return current_state in fsm.quit_states
