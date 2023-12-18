from utils import *

import numpy as np

TRENCH = "#"


def parse_in1(line: str) -> tuple[str, int]:
    direction, meters, _ = line.split()
    match direction:
        case "U": direction = North
        case "D": direction = South
        case "R": direction = East
        case "L": direction = West
        case _: assert False
    return direction, int(meters)


def flood_fill(grid: Grid):
    def flood(point: Point) -> list[Point]:
        return [add(point, d) for d in directions4
                if add(point, d) not in grid]

    frontier = {(1, 1)}
    while frontier:
        p = frontier.pop()
        grid[p] = TRENCH
        for child in flood(p):
            frontier.add(child)


def p1(text: str) -> any:
    in1 = parse(text, parse_in1, show=0)
    grid = Grid(default=".")

    digger = (0, 0)
    grid[digger] = TRENCH
    for direction, meters in in1:
        for i in range(meters):
            digger = add(digger, direction)
            grid[digger] = TRENCH

    flood_fill(grid)

    return len(grid)


def parse_in2(line: str) -> tuple[str, int]:
    meters, direction = re.findall(r"#([a-z0-9]+)([0-9])", line)[0]
    match direction:
        case "0": direction = East
        case "1": direction = South
        case "2": direction = West
        case "3": direction = North
        case _: assert False
    return direction, int(meters, 16)


def shoelace_formula(xs: list[int], ys: list[int]) -> int:
    # TODO implement by hand and remove numpy; should be fast enough
    polygon_area = np.abs(np.dot(xs, np.roll(ys, 1)) - np.dot(ys, np.roll(xs, 1))) // 2
    return int(polygon_area)  # convert from numpy int64 to int


def p2(text: str) -> any:
    in2 = parse(text, parse_in2, show=0)

    p = (0, 0)
    xs, ys = [0], [0]
    for direction, meters in in2:
        p = add(p, mul(direction, meters))
        xs.append(X_(p))
        ys.append(Y_(p))

    circumference = sum(meters for _, meters in in2)
    return shoelace_formula(xs, ys) + (circumference // 2 + 1)
