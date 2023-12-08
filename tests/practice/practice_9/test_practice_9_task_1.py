import pytest
from io import StringIO
from src.practice.practice_9.practice_9_task_1 import *
from src.practice.practice_9.fsm_module import *

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


@pytest.mark.parametrize(
    "table,functions,start_state,quit_states",
    [
        (table_ab, functions_ab, start_state_ab, quit_states_ab),
        (table_number, functions_number, start_state_number, quit_states_number),
    ],
)
def test_create_fs_machine(table, functions, start_state, quit_states):
    fsm = create_fs_machine(table, functions, start_state, quit_states)
    assert (
        fsm.table == table,
        fsm.functions == functions,
        fsm.start_state == start_state,
        fsm.quit_states == quit_states,
    )


@pytest.mark.parametrize(
    "fsm,string,expected",
    [
        (fsm_ab, "aab", False),
        (fsm_ab, "aabb", True),
        (fsm_ab, "abb", True),
        (fsm_ab, "", False),
        (fsm_number, "123.", False),
        (fsm_number, "E12", False),
        (fsm_number, "123", True),
        (fsm_number, "+123", True),
        (fsm_number, "-123", True),
        (fsm_number, "+123.12", True),
        (fsm_number, "-.12", True),
        (fsm_number, "-.12E12", True),
        (fsm_number, "-.12E+12", True),
        (fsm_number, "-.12E-12", True),
        (fsm_number, "-.12E-12", True),
        (fsm_number, "+", False),
    ],
)
def test_validate_string(fsm, string, expected):
    pass


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("aab", "aab is not any language\n"),
        ("aabb", "aabb is (a|b)*abb language\n"),
        ("abb", "abb is (a|b)*abb language\n"),
        ("", " is not any language\n"),
        ("123.", "123. is not any language\n"),
        ("E12", "E12 is not any language\n"),
        ("+", "+ is not any language\n"),
        ("123", "123 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("+123", "+123 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("-123", "-123 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("+123.12", "+123.12 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("-.12", "-.12 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("-.12E12", "-.12E12 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("-.12E+12", "-.12E+12 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("-.12E-12", "-.12E-12 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
        ("-.12E-12", "-.12E-12 is digit+(.digit+)?(E(+|-)?digit+)? language\n"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
