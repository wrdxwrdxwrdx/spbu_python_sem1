from dataclasses import dataclass


@dataclass
class FSMachine:
    name: str
    table: tuple[dict[str, int]]
    start_state: int
    terminal_states: list


def create_fs_machine(
    name: str, table: tuple[dict[str, int]], start_state: int, terminal_states: list
) -> FSMachine:
    """create fsm with table, start_state, terminal_states and functions\n
    table:\n
    [\n
    {digits: 1, ".": 3, "-+": 1},\n
    {digits: 2, ".": 3},\n
    ...\n
    ]
    """

    fsm = FSMachine(name, table, start_state, terminal_states)

    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    """check is string valid in fsm language"""
    current_state = fsm.start_state
    for token in string:
        state_rules = fsm.table[current_state]
        for rule in state_rules.keys():
            if token in rule:
                current_state = state_rules[rule]
                break
        else:
            return False
    return current_state in fsm.terminal_states
