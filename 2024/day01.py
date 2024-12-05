# start: So 01 Dez 2024 10:45:28 CET
# part1: So 01 Dez 2024 10:57:18 CET
# part2: So 01 Dez 2024 11:13:09 CET

from collections import Counter
from utils import *


def p1(text: str) -> any:
    in1 = parse(text, ints)
    xs, ys = T(in1)
    return sum([abs(x - y) for x, y in zip(sorted(xs), sorted(ys))])


def p2(text: str) -> any:
    in2 = parse(text, ints)
    xs, ys = T(in2)
    ctr = Counter(ys)
    return sum([x * ctr[x] for x in xs])
