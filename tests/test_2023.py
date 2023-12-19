from utils import get_text

from datetime import datetime, timedelta, timezone
import importlib
import pytest


@pytest.mark.parametrize("puzzle, solution", [
    (1.1, 54601),
    (1.2, 54078),
    (2.1, 2239),
    (2.2, 83435),
    (3.1, 535078),
    (3.2, 75312571),
    (4.1, 21213),
    (4.2, 8549735),
    (5.1, 510109797),
    (5.2, 9622622),
    (6.1, 2344708),
    (6.2, 30125202),
    (7.1, 246424613),
    (7.2, 248256639),
    (8.1, None),
    (8.2, None),
    (9.1, 1666172641),
    (9.2, 933),
    (10.1, None),
    (10.2, None),
    (11.1, 10276166),
    (11.2, 598693078798),
    (12.1, 7118),
    (12.2, None),
    (13.1, None),
    (13.2, None),
    (14.1, 110821),
    (14.2, None),
    (15.1, 505459),
    (15.2, 228508),
    (16.1, None),
    (16.2, None),
    (17.1, None),
    (17.2, None),
    (18.1, 31171),
    (18.2, 131431655002266),
    (19.1, 398527),
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
