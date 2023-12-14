from utils import *

ROUND = "O"
CUBE = "#"
EMPTY = "."


def p1(text: str) -> any:
    in1 = parse(text)
    grid = Grid(in1, skip=(EMPTY, ))

    load = 0
    for col in T(grid.to_rows()):
        stop = 0
        for i in range(len(col)):
            match col[i]:
                case "#":
                    stop = i + 1
                case "O":
                    load += len(col) - stop
                    stop += 1

    return load
