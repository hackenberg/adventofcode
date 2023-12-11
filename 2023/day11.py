from utils import *

GALAXY = "#"
EMPTY_SPACE = "."


def expand_grid(grid: Grid) -> tuple[list[int], list[int]]:
    expand_cols = []
    for x in cover(Xs(grid)):
        col = flatten(grid.to_rows(xrange=cover((x,))))
        if GALAXY not in col:
            expand_cols.append(x)

    expand_rows = []
    for y in cover(Ys(grid)):
        row = flatten(grid.to_rows(yrange=cover((y,))))
        if GALAXY not in row:
            expand_rows.append(y)

    return expand_cols, expand_rows


def galaxy_distance(p, q, expand_rows, expand_cols, expansion=1):
    expand_rows = len([r for r in expand_rows if r in cover(Ys((p, q)))])
    expand_cols = len([c for c in expand_cols if c in cover(Xs((p, q)))])
    return manhattan_distance(p, q) + expansion * (expand_rows + expand_cols)


def p1(text: str) -> any:
    grid = Grid(text, skip=(EMPTY_SPACE,), default=EMPTY_SPACE)
    expand_cols, expand_rows = expand_grid(grid)
    return sum(
        galaxy_distance(a, b, expand_rows, expand_cols)
        for a, b in combinations(grid.keys(), 2)
    )


def p2(text: str) -> any:
    grid = Grid(text, skip=(EMPTY_SPACE,), default=EMPTY_SPACE)
    expand_cols, expand_rows = expand_grid(grid)
    return sum(
        galaxy_distance(a, b, expand_rows, expand_cols, 999999)
        for a, b in combinations(grid.keys(), 2)
    )
