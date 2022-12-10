import math
#import IPython; IPython.embed(colors="neutral")
#import ipdb; ipdb.set_trace()


class Point(tuple):
    def __add__(self, other):
        return Point(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        return Point(a - b for a, b in zip(self, other))


DIRS = {
    "U": Point((0, 1)),
    "D": Point((0, -1)),
    "L": Point((-1, 0)),
    "R": Point((1, 0)),
}


def move(head, tail, direction):
    if distance(head, tail) < 2:
        return tail

    match direction:
        case "U":
            return head + DIRS["D"]
        case "D":
            return head + DIRS["U"]
        case "L":
            return head + DIRS["R"]
        case "R":
            return head + DIRS["L"]


def distance(head, tail):
    dx, dy = map(abs, head - tail)
    return math.sqrt(dx**2 + dy**2)


def p1(f):
    lines = f.read().splitlines()
    head, tail = Point((0, 0)), Point((0, 0))
    visited = set()

    for line in lines:
        direction, steps = line.split()
        for i in range(int(steps)):
            head += DIRS[direction]
            tail = move(head, tail, direction)
            visited.add(tail)

    return len(visited)


def move2(head, tail):
    corr = Point(cutoff(x) for x in head - tail)
    if corr == (head - tail):
        return tail
    return tail + corr


def cutoff(x):
    return min(1, max(-1, x))


def p2(f):
    lines = f.read().splitlines()
    rope = [Point((0, 0))] * 10
    visited = set()

    for line in lines:
        direction, steps = line.split()
        for i in range(int(steps)):
            rope[0] += DIRS[direction]
            for i in range(1, len(rope)):
                rope[i] = move2(rope[i-1], rope[i])
            visited.add(rope[-1])

    return len(visited)
