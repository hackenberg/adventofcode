from utils import get_text
from testutils import *

import importlib
import pytest


@pytest.mark.parametrize("puzzle, solution", [
    (1.1, 1696),
    (1.2, 1737),
    (2.1, 1480518),
    (2.2, 1282809906),
    (3.1, 749376),
    (3.2, 2372923),
    skip(4.1, 0),
    skip(4.2, 0),
    skip(5.1, 6283),
    skip(5.2, None),
    (6.1, 386755),
    (6.2, 1732731810807),
    xfail(7.1, None),
    xfail(7.2, None),
    xfail(8.1, None),
    xfail(8.2, None),
    xfail(9.1, None),
    xfail(9.2, None),
    xfail(10.1, None),
    xfail(10.2, None),
    xfail(11.1, None),
    xfail(11.2, None),
    xfail(12.1, None),
    xfail(12.2, None),
    xfail(13.1, None),
    xfail(13.2, None),
    xfail(14.1, None),
    xfail(14.2, None),
    xfail(15.1, None),
    xfail(15.2, None),
    xfail(16.1, None),
    xfail(16.2, None),
    xfail(17.1, None),
    xfail(17.2, None),
    xfail(18.1, None),
    xfail(18.2, None),
    xfail(19.1, None),
    xfail(19.2, None),
    xfail(20.1, None),
    xfail(20.2, None),
    xfail(21.1, None),
    xfail(21.2, None),
    xfail(22.1, None),
    xfail(22.2, None),
    xfail(23.1, None),
    xfail(23.2, None),
    xfail(24.1, None),
    xfail(24.2, None),
    xfail(25.1, None),
    xfail(25.2, None),
])
def test_answer(puzzle: float, solution: int):
    code = get_code(puzzle)
    assert code() == solution


def get_code(puzzle: float) -> callable:
    day, part = [int(n) for n in str(puzzle).split(".")]
    assert 1 <= day <= 25
    assert part in (1, 2)
    module = importlib.import_module(f"2021.day{day:02}")
    func = getattr(module, f"p{part}")
    text = get_text(day)
    return lambda: func(text)
