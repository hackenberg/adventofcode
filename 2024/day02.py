# start: Mo 02 Dez 2024 10:05:30 CET
# part1: Mo 02 Dez 2024 11:00:22 CET
# part2: Mo 02 Dez 2024 11:11:55 CET

from utils import *


def p1(text: str) -> any:
    in1 = parse(text, ints)
    return sum(_is_safe(report) for report in in1)


def _is_safe(r):
    return _is_gradual(r) and (is_ascending(r) or is_descending(r))


def _is_gradual(seq):
    return all(
        abs(seq[i] - seq[i+1]) < 4
        for i in range(len(seq) - 1)
    )


def p2(text: str) -> any:
    in1 = parse(text, ints)
    return sum(_is_safe_p2(report) for report in in1)


def _is_safe_p2(r):
    if _is_safe(r):
        return True
    for i in range(len(r)):
        if _is_safe(r[:i] + r[i+1:]):
            return True
    return False
