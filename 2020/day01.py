from functools import reduce
from itertools import combinations


def p1(f):
    return solution(f, 2)


def p2(f):
    return solution(f, 3)


def solution(f, n):
    entries = [int(s) for s in f.read().splitlines()]
    for cs in combinations(entries, n):
        if sum(cs) == 2020:
            return reduce(lambda x, y: x * y, cs)
