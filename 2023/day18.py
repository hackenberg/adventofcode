from utils import *

TRENCH = "#"


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


def parse_in1(line: str) -> tuple[str, int]:
    direction, meters, _ = line.split()
    match direction:
        case "U": direction = North
        case "D": direction = South
        case "R": direction = East
        case "L": direction = West
        case _: assert False
    return direction, int(meters)


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
