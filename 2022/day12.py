from aoc import manhattan_distance, Point


class Node(Point):
    def __init__(self, iterable=(), goal=None, parent=None):
        Point.__init__(iterable)
        self.goal = goal
        self.parent = parent

    def successors(self):
        return map(
            lambda d: Node(self + d, goal=self.goal, parent=self),
            [(1,0), (0,1), (-1,0), (0,-1)]
        )

    @property
    def f(self):
        return self.g + self.h

    @property
    def g(self):
        if self.parent is None:
            return 0
        return self.parent.g + 1

    @property
    def h(self):
        return manhattan_distance(self, self.goal)


def p1(f):
    grid = {
        (i, j): x
        for i, row in enumerate(f.read().splitlines())
        for j, x in enumerate(row)
    }

    S = next(k for k, v in grid.items() if v == "S")
    E = next(k for k, v in grid.items() if v == "E")

    grid[S] = "a"
    grid[E] = "z"

    open_lst = [Node(S, goal=E)]
    closed_lst = []

    while len(open_lst) > 0:
        p = open_lst.pop()
        for q in p.successors():
            if ord(grid.get(q, "~")) - ord(grid.get(p)) > 1:
                continue

            if q == E:
                return q.g

            if len([n for n in open_lst if n == q and n.f <= q.f]) > 0:
                continue

            if len([n for n in closed_lst if n == q and n.f <= q.f]) > 0:
                continue

            open_lst.append(q)

        open_lst.sort(key=lambda n: n.f, reverse=True)
        closed_lst.append(p)


def p2(f):
    pass
