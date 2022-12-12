class Point(tuple):
    def __add__(self, other):
        return Point(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        return Point(a - b for a, b in zip(self, other))


def manhattan_distance(p1, p2):
    return sum(map(abs, p1 - p2))
