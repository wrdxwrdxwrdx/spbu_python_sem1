from src.homeworks.homework_5.homework_5_task_1 import *
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "char,expected", [("H", "U+0048"), ("e", "U+0065"), (",", "U+002C")]
)
def test_get_unicode(char, expected):
    assert get_unicode(char) == expected


@pytest.mark.parametrize(
    "char,expected",
    [
        ("H", "00000000 00000000 00000000 01001000"),
        ("e", "00000000 00000000 00000000 01100101"),
        (",", "00000000 00000000 00000000 00101100"),
    ],
)
def test_get_unicode_binary(char, expected):
    assert get_unicode_binary(char) == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (
            "Hello, World!",
            [
                "H   U+0048  00000000 00000000 00000000 01001000",
                "e   U+0065  00000000 00000000 00000000 01100101",
                "l   U+006C  00000000 00000000 00000000 01101100",
                "l   U+006C  00000000 00000000 00000000 01101100",
                "o   U+006F  00000000 00000000 00000000 01101111",
                ",   U+002C  00000000 00000000 00000000 00101100",
                "    U+0020  00000000 00000000 00000000 00100000",
                "W   U+0057  00000000 00000000 00000000 01010111",
                "o   U+006F  00000000 00000000 00000000 01101111",
                "r   U+0072  00000000 00000000 00000000 01110010",
                "l   U+006C  00000000 00000000 00000000 01101100",
                "d   U+0064  00000000 00000000 00000000 01100100",
                "!   U+0021  00000000 00000000 00000000 00100001",
                "",
            ],
        ),
        (
            "Lorem Ipsum",
            [
                "L   U+004C  00000000 00000000 00000000 01001100",
                "o   U+006F  00000000 00000000 00000000 01101111",
                "r   U+0072  00000000 00000000 00000000 01110010",
                "e   U+0065  00000000 00000000 00000000 01100101",
                "m   U+006D  00000000 00000000 00000000 01101101",
                "    U+0020  00000000 00000000 00000000 00100000",
                "I   U+0049  00000000 00000000 00000000 01001001",
                "p   U+0070  00000000 00000000 00000000 01110000",
                "s   U+0073  00000000 00000000 00000000 01110011",
                "u   U+0075  00000000 00000000 00000000 01110101",
                "m   U+006D  00000000 00000000 00000000 01101101",
                "",
            ],
        ),
        (
            "😀😁",
            [
                "😀   U+1F600  00000000 00000001 11110110 00000000",
                "😁   U+1F601  00000000 00000001 11110110 00000001",
                "",
            ],
        ),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output.split("\n") == expected
