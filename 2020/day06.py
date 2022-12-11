from collections import defaultdict
from functools import reduce


def p1(f):
    groups = f.read().split("\n\n")
    answers = defaultdict(set)

    for i, group in enumerate(groups):
        persons = [set(p) for p in group.splitlines()]
        answers[i] = reduce(lambda a, b: a.union(b), persons)

    return sum(map(len, answers.values()))


def p2(f):
    groups = f.read().split("\n\n")
    answers = defaultdict(list)

    for i, group in enumerate(groups):
        persons = [set(p) for p in group.splitlines()]
        answers[i] = reduce(lambda a, b: a.intersection(b), persons)

    return sum(map(len, answers.values()))
