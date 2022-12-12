import math


def p1(f):
    lines = f.read().splitlines()
    return count_trees(lines, (1, 3))


def p2(f):
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]

    lines = f.read().splitlines()
    return math.prod(count_trees(lines, s) for s in slopes)


def count_trees(lines, slope):
    drow, dcol = slope
    col = 0
    trees = 0

    for row in range(0, len(lines), drow):
        if lines[row][col] == "#":
            trees += 1
        col = (col + dcol) % len(lines[row])

    return trees
