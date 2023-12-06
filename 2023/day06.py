from utils import *


def ways_to_win(time: int, distance: int) -> int:
    return sum(x * y > distance for x, y in enumerate(range(time, 0, -1)))


def p1(text: str) -> any:
    in1 = parse(text, ints)
    return prod(ways_to_win(*race) for race in zip(*in1))


def parse_line(line: str) -> int:
    _, values = line.split(":")
    return int("".join(values.split()))


def p2(text: str) -> any:
    in2 = parse(text, parse_line)
    return ways_to_win(*in2)
