from functools import reduce
from utils import *


def p1(text: str) -> any:
    grid = Grid(text, skip=(".",), default=".")

    frequencies = defaultdict(set)
    reduce(lambda _, e: frequencies[e[1]].add(e[0]), grid.items(), None)

    antinodes = set()
    for frequency, locations in frequencies.items():
        for p, q in permutations(locations, r=2):
            a = add(q, sub(q, p))
            if grid.in_range(a):
                antinodes.add(a)

    return len(antinodes)


def p2(text: str) -> any:
    grid = Grid(text, skip=(".",), default=".")

    frequencies = defaultdict(set)
    reduce(lambda _, e: frequencies[e[1]].add(e[0]), grid.items(), None)

    antinodes = set()
    for frequency, locations in frequencies.items():
        for p, q in permutations(locations, r=2):
            d = sub(q, p)

            antinodes.add(p)
            antinodes.add(q)

            a = add(q, d)
            while grid.in_range(a):
                antinodes.add(a)
                a = add(a, d)

    return len(antinodes)
