import json
from functools import cmp_to_key


def compare(left, right):
    if type(left) == int and type(right) == int:
        return left - right

    if type(left) == int:
        return compare([left], right)
    if type(right) == int:
        return compare(left, [right])

    for pair in zip(left, right):
        comparison = compare(*pair)
        if comparison:
            return comparison

    return len(left) - len(right)


def p1(f):
    pairs = [p.splitlines() for p in f.read().split("\n\n")]

    i, solution = 1, 0

    for pair in pairs:
        left, right = [json.loads(p) for p in pair]
        if compare(left, right) < 0:
            solution += i
        i += 1

    return solution


def p2(f):
    packets = [json.loads(p) for p in f.read().splitlines() if p != ""]
    d1, d2 = [[2]], [[6]]

    packets = sorted(packets + [d1, d2], key=cmp_to_key(compare))

    return (packets.index(d1) + 1) * (packets.index(d2) + 1)
