from utils import get_text
from testutils import *

from datetime import datetime, timedelta, timezone
import importlib
import pytest


@pytest.mark.parametrize("puzzle, solution", [
    (1.1, 54601),
    (1.2, 54078),
    (2.1, 2239),
    (2.2, 83435),
    (3.1, None),
    (3.2, None),
    (4.1, None),
    (4.2, None),
    (5.1, None),
    (5.2, None),
    (6.1, None),
    (6.2, None),
    (7.1, None),
    (7.2, None),
    (8.1, None),
    (8.2, None),
    (9.1, None),
    (9.2, None),
    (10.1, None),
    (10.2, None),
    (11.1, None),
    (11.2, None),
    (12.1, None),
    (12.2, None),
    (13.1, None),
    (13.2, None),
    (14.1, None),
    (14.2, None),
    (15.1, None),
    (15.2, None),
    (16.1, None),
    (16.2, None),
    (17.1, None),
    (17.2, None),
    (18.1, None),
    (18.2, None),
    (19.1, None),
    (19.2, None),
    (20.1, None),
    (20.2, None),
    (21.1, None),
    (21.2, None),
    (22.1, None),
    (22.2, None),
    (23.1, None),
    (23.2, None),
    (24.1, None),
    (24.2, None),
    (25.1, None),
    (25.2, None),
])
def test_answer(puzzle: float, solution: int):
    day, part = [int(n) for n in str(puzzle).split(".")]
    now = datetime.now(timezone(timedelta(hours=-5)))
    if day > now.day:
        pytest.xfail("Puzzle not yet released")
    if solution is None:
        pytest.xfail("Solution not provided")
    code = get_code(day, part)
    assert code() == solution


def get_code(day: int, part: int) -> callable:
    assert 1 <= day <= 25
    assert part in (1, 2)
    module = importlib.import_module(f"2023.day{day:02}")
    func = getattr(module, f"p{part}")
    text = get_text(day)
    return lambda: func(text)
