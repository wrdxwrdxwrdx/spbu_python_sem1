import pytest
from io import StringIO
from src.practice.practice_9.practice_9_task_1 import *
from src.practice.practice_9.fsm_module import *


@pytest.mark.parametrize(
    "name,table,start_state,terminal_states",
    [
        ("aabb", ({"a": 1}, {"b": 0}), 0, [3]),
        (
            "number",
            ({"a": 1}, {"b": 0}),
            0,
            [2, 4, 7],
        ),
    ],
)
def test_create_fs_machine(name, table, start_state, terminal_states):
    fsm = create_fs_machine(name, table, start_state, terminal_states)
    assert (
        fsm.name == name,
        fsm.table == table,
        fsm.start_state == start_state,
        fsm.terminal_states == terminal_states,
    )


@pytest.mark.parametrize(
    "fsm,string,expected",
    [
        (create_fsm_ab(), "aab", False),
        (create_fsm_ab(), "aabb", True),
        (create_fsm_ab(), "abb", True),
        (create_fsm_ab(), "", False),
        (create_fsm_number(), "123.", False),
        (create_fsm_number(), "E12", False),
        (create_fsm_number(), "123", True),
        (create_fsm_number(), "+123", True),
        (create_fsm_number(), "-123", True),
        (create_fsm_number(), "+123.12", True),
        (create_fsm_number(), "-.12", True),
        (create_fsm_number(), "-.12E12", True),
        (create_fsm_number(), "-.12E+12", True),
        (create_fsm_number(), "-.12E-12", True),
        (create_fsm_number(), "-.12E-12", True),
        (create_fsm_number(), "+", False),
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
