from itertools import product
from math import prod


def p1(f):
    trees = f.read().splitlines()
    xlen, ylen = len(trees[0]), len(trees)
    visible = set()

    trees = list(map(list, trees))

    for y in range(ylen):
        tallest = None
        for x in range(xlen):
            trees[y][x] = int(trees[y][x])
            if tallest is None or trees[y][x] > tallest:
                tallest = trees[y][x]
                visible.add((x,y))

    for y in range(ylen):
        tallest = None
        for x in range(xlen-1, -1, -1):
            if tallest is None or trees[y][x] > tallest:
                tallest = trees[y][x]
                visible.add((x,y))

    for x in range(xlen):
        tallest = None
        for y in range(ylen):
            if tallest is None or trees[y][x] > tallest:
                tallest = trees[y][x]
                visible.add((x,y))

    for x in range(xlen):
        tallest = None
        for y in range(ylen-1, -1, -1):
            if tallest is None or trees[y][x] > tallest:
                tallest = trees[y][x]
                visible.add((x,y))

    return len(visible)


def p2(f):
    trees = f.read().splitlines()
    xlen, ylen = len(trees[0]), len(trees)

    def scenic_score(x0, y0):
        vd_up = 0
        for y in range(y0-1, -1, -1):
            vd_up += 1
            if trees[y][x0] >= trees[y0][x0]:
                break

        vd_left = 0
        for x in range(x0-1, -1, -1):
            vd_left += 1
            if trees[y0][x] >= trees[y0][x0]:
                break

        vd_down = 0
        for y in range(y0+1, ylen):
            vd_down += 1
            if trees[y][x0] >= trees[y0][x0]:
                break

        vd_right = 0
        for x in range(x0+1, xlen):
            vd_right += 1
            if trees[y0][x] >= trees[y0][x0]:
                break

        return prod([vd_up, vd_left, vd_down, vd_right])

    return max(scenic_score(*pos) for pos in product(range(ylen), range(xlen)))
