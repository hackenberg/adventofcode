import math
from collections import deque
#import IPython; IPython.embed(colors="neutral")
#import ipdb; ipdb.set_trace()


class Grid:
    def __init__(self):
        self.head = (0,0)
        self.tail = (0,0)
        self.visited = set()

    def move(self, direction):
        assert direction in ["U", "D", "L", "R"]
        match direction:
            case "U":
                self.head = add(self.head, (0,1))
                if self.distance >= 2:
                    self.tail = add(self.head, (0,-1))
            case "D":
                self.head = add(self.head, (0, -1))
                if self.distance >= 2:
                    self.tail = add(self.head, (0,1))
            case "L":
                self.head = add(self.head, (-1, 0))
                if self.distance >= 2:
                    self.tail = add(self.head, (1,0))
            case "R":
                self.head = add(self.head, (1, 0))
                if self.distance >= 2:
                    self.tail = add(self.head, (-1,0))

        self.visited.add(self.tail)

    @property
    def distance(self):
        dx = abs(self.head[0] - self.tail[0])
        dy = abs(self.head[1] - self.tail[1])
        return math.sqrt(dx**2 + dy**2)


def add(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))


def p1(f):
    lines = f.read().splitlines()
    grid = Grid()

    for line in lines:
        direction, steps = line.split()
        for i in range(int(steps)):
            grid.move(direction)

    return len(grid.visited)


def p2(f):
    pass
