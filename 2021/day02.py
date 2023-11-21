from collections import defaultdict, deque
from utils       import *


def p1(text):
    lines = parse(text)
    xpos, zpos = 0, 0

    for line in lines:
        match line.split():
            case ["forward", n]:
                xpos += int(n)
            case ["down", n]:
                zpos += int(n)
            case ["up", n]:
                zpos -= int(n)

    return xpos * zpos


def p2(text):
    lines = parse(text)
    xpos, zpos, aim = 0, 0, 0

    for line in lines:
        match line.split():
            case ["forward", n]:
                xpos += int(n)
                zpos += int(n) * aim
            case ["down", n]:
                aim += int(n)
            case ["up", n]:
                aim -= int(n)

    return xpos * zpos
