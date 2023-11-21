from collections import defaultdict, deque
from utils       import *


def p1(text: str):
    xs = parse(text, int)
    return sum(x < y for x, y in zip(xs, xs[1:]))


def p2(text: str):
    xs = parse(text, int)
    ts = [sum(t) for t in zip(xs, xs[1:], xs[2:])]
    return sum(a < b for a, b in zip(ts, ts[1:]))
