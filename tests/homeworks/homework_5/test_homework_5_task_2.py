from src.homeworks.homework_5.homework_5_task_2.dna_functions import *
import pytest


@pytest.mark.parametrize(
    "dna_code,expected", [("d2c4a5", True), ("dd2c5a3", False), ("a3b1", True)]
)
def test_is_valid_dna_code(dna_code, expected):
    assert is_valid_dna_code(dna_code) == expected


@pytest.mark.parametrize(
    "dna,expected", [("aaa3bbc", False), ("aabc", True), ("AAaBBb", True), ("", False)]
)
def test_is_valid_dna(dna, expected):
    assert is_valid_dna(dna) == expected


@pytest.mark.parametrize(
    "dna,expected",
    [("aaabbcaa", "a3b2c1a2"), ("aabc", "a2b1c1"), ("AAaBBb", "A2a1B2b1")],
)
def test_encode(dna, expected):
    assert encode(dna) == expected


@pytest.mark.parametrize(
    "dna_code,expected",
    [("a3b2c1a2", "aaabbcaa"), ("a2b1c1", "aabc"), ("A2a1B2b1", "AAaBBb")],
)
def test_decode(dna_code, expected):
    assert decode(dna_code) == expected


@pytest.mark.parametrize(
    "dna_code", [("a2b3c"), ("a"), ("4a2b4"), ("1a2b"), ("a0b2"), ("ф2а2")]
)
def test_is_valid_dna_code(dna_code):
    with pytest.raises(ValueError):
        is_valid_dna_code(dna_code)


@pytest.mark.parametrize("dna", [("ффффллл"), ("абв")])
def test_is_valid_dna(dna):
    with pytest.raises(ValueError):
        is_valid_dna(dna)


@pytest.mark.parametrize("dna", [("aaa2bbb"), ("2ab2"), ("a22a")])
def test_encode(dna):
    with pytest.raises(ValueError):
        encode(dna)


@pytest.mark.parametrize("dna_code", [("aa2b3"), ("a2b3cc2")])
def test_decode(dna_code):
    with pytest.raises(ValueError):
        decode(dna_code)
