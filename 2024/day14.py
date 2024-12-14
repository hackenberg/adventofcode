from pprint import pprint
from utils import *

#import IPython; IPython.embed(colors="neutral")
#import ipdb; ipdb.set_trace()

Robot = namedtuple("Robot", ["px", "py", "vx", "vy"])


def p1(text: str) -> any:
    robots = parse(text, ints)

    #xrange = 11
    #yrange = 7
    xrange = 101
    yrange = 103
    ticks = 100

    robots = [
        (moveN(px, vx, xrange, ticks), moveN(py, vy, yrange, ticks))
        for px, py, vx, vy in robots
    ]

    quadrants = (
        [p for p in robots if X_(p) < xrange // 2 and Y_(p) < yrange // 2], 
        [p for p in robots if X_(p) < xrange // 2 and Y_(p) > yrange // 2], 
        [p for p in robots if X_(p) > xrange // 2 and Y_(p) > yrange // 2], 
        [p for p in robots if X_(p) > xrange // 2 and Y_(p) < yrange // 2], 
    )

    return prod(len(q) for q in quadrants)


def moveN(p: int, v: int, r: int, n: int) -> int:
    pnext = p + n * v
    if pnext < 0:
        pnext += ceil((pnext * -1) / r) * r
    if pnext >= r:
        pnext %= r
    return pnext


def p2(text: str) -> any:
    robots = parse(text, ints)

    xrange = 101
    yrange = 103
    ticks = 100

    robots = [
        (moveN(px, vx, xrange, ticks), moveN(py, vy, yrange, ticks), vx, vy)
        for px, py, vx, vy in robots
    ]

    i = 0
    while True:
        print(f"i={i}")
        g = Grid(Counter((px, py) for px, py, _, _ in robots), default=".")
        g.print()
        robots = [
            (moveN(px, vx, xrange, 1), moveN(py, vy, yrange, 1), vx, vy)
            for px, py, vx, vy in robots
        ]
        i += 1
        input("Press Enter to continue...")


