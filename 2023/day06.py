from utils import *


def ways_to_win(time: int, distance: int) -> int:
    return sum((x * (time - x)) > distance for x in range(time))


def p1(text: str) -> any:
    in1 = parse(text, ints)
    return prod(ways_to_win(*race) for race in zip(*in1))


def parse_line(line: str) -> int:
    _, values = line.split(":")
    return int("".join(values.split()))


def p2(text: str) -> any:
    in2 = parse(text, parse_line)
    return ways_to_win(*in2)
