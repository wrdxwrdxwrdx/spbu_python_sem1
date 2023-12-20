import pytest

from src.test.test_2.test_2_task_2.task_2 import logger
from unittest.mock import patch
import tempfile


@pytest.mark.parametrize(
    "function,expected",
    [
        ("dummy_func(1, 2, 3)", "20/12/2023 03:43:20 dummy_func a=1 b=2 c=3 6"),
        (
            "dummy_func(c=3, a=1, b=2)",
            "20/12/2023 03:43:20 dummy_func a=1 b=2 c=3 6",
        ),
        ("dummy_func(5, 5)", "20/12/2023 03:43:20 dummy_func a=5 b=5 c=3 13"),
    ],
)
def test_main_scenario(function, expected):
    directory = tempfile.TemporaryDirectory()
    file = tempfile.NamedTemporaryFile()

    @logger(file.name)
    def dummy_func(a, b, c=3):
        return a + b + c

    with patch("src.test.test_2.test_2_task_2.task_2.time.localtime") as mock_date:
        mock_date.return_value = (2023, 12, 20, 3, 43, 20, 2, 354, 0)
        eval(function)
    with open(file.name) as output:
        assert output.readline().strip() == expected
