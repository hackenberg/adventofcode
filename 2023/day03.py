from utils import *

Point = Tuple[int, ...]

directions4 = East, South, West, North = ((1, 0), (0, 1), (-1, 0), (0, -1))
diagonals = SE, NE, SW, NW = ((1, 1), (1, -1), (-1, 1), (-1, -1))
directions8 = directions4 + diagonals

def X_(point: Point) -> int: "X coordinate of a point"; return point[0]
def Y_(point: Point) -> int: "Y coordinate of a point"; return point[1]

def Xs(points: Iterable[Point]) -> Tuple[int]:
    """X coordinates of a collection of points"""
    return mapt(X_, points)

def Ys(points: Iterable[Point]) -> Tuple[int]:
    """Y coordinates of a collection of points"""
    return mapt(Y_, points)

def add(p: Point, q: Point) -> Point: return mapt(operator.add, p, q)


class Grid(dict):
    def __init__(self, grid, skip=()):
        super().__init__()
        self.update({(x, y): val
                     for y, row in enumerate(grid)
                     for x, val in enumerate(row)
                     if val not in skip})

    def neighbors(self, point: Point) -> List[Point]:
        """Points on the grid that neighbor `point`."""
        return [add(point, d) for d in directions8
                if add(point, d) in self]

    def neighbor_contents(self, point: Point) -> Iterable:
        """The contents of the neighboring points."""
        return (self[p] for p in self.neighbors(point))

    def to_rows(self, xrange=None, yrange=None) -> List[List[any]]:
        """The contents of the grid, as a rectangular list of lists.
           You can define a window with an xrange and yrange; or they default to the whole grid."""
        xrange = xrange or cover(Xs(self))
        yrange = yrange or cover(Ys(self))
        return [[self.get((x, y)) for x in xrange]
                for y in yrange]


def p1(text: str) -> any:
    in1 = parse(text)
    grid = Grid(in1, skip=(".",))
    ans = 0
    for y, row in enumerate(in1):
        idx = 0
        for n in re.findall("[0-9]+", row):
            idx = row.index(n, idx)
            n_points = tuple((x, y) for x in range(idx, idx+len(n)))
            n_neighbors = set(flatten(grid.neighbors(p) for p in n_points))
            n_neighbor_symbols = [grid[p] for p in n_neighbors if not grid[p].isdigit()]
            if len(n_neighbor_symbols) > 0:
                ans += int(n)
            idx += 1

    return ans


def p2(text: str) -> any:
    in2 = parse(text)
    grid = Grid(in2, skip=(".",))
    gears = [p for p, sym in grid.items() if sym == "*"]
    gear_ratios = []
    for gear in gears:
        neighbor_digits = [p for p in grid.neighbors(gear) if grid[p].isdigit()]
        neighbor_numbers = {expand_number(p, grid) for p in neighbor_digits}
        if len(neighbor_numbers) < 2:
            continue
        gear_ratio = prod(neighbor_numbers)
        gear_ratios.append(gear_ratio)
    return sum(gear_ratios)


def expand_number(point: Point, grid: Grid) -> int:
    # search backwards
    start = point
    while (add(start, West) in grid.keys()) and (grid[add(start, West)].isdigit()):
        start = add(start, West)

    # search forwards
    end = point
    while (add(end, East) in grid.keys()) and (grid[add(end, East)].isdigit()):
        end = add(end, East)

    xrange = cover(X_(start), X_(end))
    yrange = cover((Y_(point),))
    digits = the(grid.to_rows(xrange=xrange, yrange=yrange))
    return int("".join(digits))
