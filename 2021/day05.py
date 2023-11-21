from collections import defaultdict
from utils       import *


def p1(text):
    points = defaultdict(int)
    for x1, y1, x2, y2 in parse(text, ints):
        if x1 == x2:
            for y in cover(y1, y2):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in cover(x1, x2):
                points[(x, y1)] += 1
        else:
            pass

    return len([k for k, v in points.items() if v > 1])


def p2(text):
    points = defaultdict(int)
    for x1, y1, x2, y2 in parse(text, ints):
        print(f"{(x1, y1)} -> {(x2, y2)}")
        if x1 == x2:
            for y in cover(y1, y2):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in cover(x1, x2):
                points[(x, y1)] += 1
        elif abs(x1 - y1) == abs(x2 - y2):
            #import IPython; IPython.embed(colors="neutral")
            #import ipdb; ipdb.set_trace()
            for x, y in zip(stepto(x1, x2), stepto(y1, y2)):
                points[x, y] += 1
                print(f"{(x, y)} -> {points[(x,y)]}")
        else:
            pass

    for k, v in points.items():
        print(k, v)
    return len([k for k, v in points.items() if v > 1])


def sign(n): return -1 if n < 0 else 1


def stepto(x1, x2):
    step = sign(x2 - x1)
    return range(x1, x2 + step, step)
