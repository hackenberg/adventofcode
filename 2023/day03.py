from utils import *


def p1(text: str) -> any:
    in1 = parse(text)
    grid = Grid(in1, directions=directions8, skip=(".",), default=".")
    ans = 0
    for y, row in enumerate(in1):
        idx = 0
        for n in re.findall("[0-9]+", row):
            idx = row.index(n, idx)
            n_points = tuple((x, y) for x in range(idx, idx+len(n)))
            n_neighbors = set(flatten(grid.neighbors(p) for p in n_points))
            n_neighbor_symbols = [grid[p] for p in n_neighbors if not grid[p].isdigit()]
            if len(n_neighbor_symbols) > 0:
                ans += int(n)
            idx += 1

    return ans


def p2(text: str) -> any:
    in2 = parse(text)
    grid = Grid(in2, directions=directions8, skip=(".",), default=".")
    gears = [p for p, sym in grid.items() if sym == "*"]
    gear_ratios = []
    for gear in gears:
        neighbor_digits = [p for p in grid.neighbors(gear) if grid[p].isdigit()]
        neighbor_numbers = {expand_number(p, grid) for p in neighbor_digits}
        if len(neighbor_numbers) < 2:
            continue
        gear_ratio = prod(neighbor_numbers)
        gear_ratios.append(gear_ratio)

    return sum(gear_ratios)


def expand_number(point: Point, grid: Grid) -> int:
    # search backwards
    start = point
    while (add(start, West) in grid.keys()) and (grid[add(start, West)].isdigit()):
        start = add(start, West)

    # search forwards
    end = point
    while (add(end, East) in grid.keys()) and (grid[add(end, East)].isdigit()):
        end = add(end, East)

    xrange = cover(Xs((start, end)))
    yrange = cover((Y_(point),))
    digits = the(grid.to_rows(xrange=xrange, yrange=yrange))

    return int("".join(digits))
