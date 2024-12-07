from utils import *

moves = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

turns = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


def p1(text: str) -> any:
    in1 = parse(text)

    grid = Grid(in1)
    guard, direction = find_start(in1)
    visited = set()

    try:
        while True:
            visited.add(guard)
            guard, direction = step(guard, direction, grid)
    except KeyError:
        pass

    return len(visited)

def find_start(in1):
    for ypos, line in enumerate(in1):
        if "^" in line:
            xpos = line.index("^")
            direction = "^"
            break
        if ">" in line:
            direction = ">"
            xpos = line.index(">")
            break
        if "v" in line:
            direction = "<"
            xpos = line.index("v")
            break
        if "<" in line:
            direction = "v"
            xpos = line.index("<")
            break
    return (xpos, ypos), direction


def step(guard, direction, grid):
    nextpos = add(guard, moves[direction])
    if grid[nextpos] == "#":
        direction = turns[direction]
    return add(guard, moves[direction]), direction


def p2(text: str) -> any:
    in1 = parse(text)
    grid = Grid(in1)
    guard, direction = find_start(in1)
    visited = set()

    try:
        while True:
            visited.add(guard)
            guard, direction = step(guard, direction, grid)

            if guard in visited:
                print("intersection:", guard)
    except KeyError:
        pass

    return len(visited)
    #import IPython; IPython.embed(colors="neutral")
    #import ipdb; ipdb.set_trace()


