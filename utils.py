"""Heavily inspired by Peter Norvigs AdventUtils.
see: https://github.com/norvig/pytudes/blob/main/ipynb/AdventUtils.ipynb
"""
from collections import Counter, defaultdict, deque, namedtuple
from itertools   import chain, count, groupby
from math        import inf, prod
from pathlib     import Path
from typing      import Callable, Iterable, List, Sequence, Set, Tuple, TypeVar, Union

import operator
import re

T = TypeVar("T")

INPUT_DIR = Path(__file__).parent / "input"
YEAR = "2023"

lines = str.splitlines
def paragraphs(text: str) -> list[str]: return text.split("\n\n")


def parse(day_or_text, parser: callable = str, sections: callable = lines, sample: bool = False) -> tuple:
    text = get_text(day_or_text, sample)
    return mapt(parser, sections(text.rstrip()))


def get_text(day_or_text: Union[int, str], sample: bool = False) -> str:
    if isinstance(day_or_text, str):
        return day_or_text

    suffix = "_sample" if sample else ""
    input_file = INPUT_DIR / YEAR / f"day{day_or_text:02}{suffix}.txt"
    return input_file.read_text()


def show_items(source, items, show: int, hr="─"*100):
    """Show the first few items, in a pretty format."""
    if show:
        types = Counter(map(type, items))
        counts = ", ".join(f"{n} {t.__name__}{'' if n == 1 else 's'}" for t, n in types.items())
        print(f"\n{hr}\n{source} ➜ {counts}:\n{hr}")
        for line in items[:show]:
            print(truncate(line))
        if show < len(items):
            print('...')


"""Functions that can be used as the parser argument:"""

def ints(text: str) -> tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'-?[0-9]+', text))


"""Helper functions:"""

def truncate(object, width=100, ellipsis=' ...') -> str:
    """Use ellipsis to truncate `str(object)` to `width` characters, if necessary."""
    string = str(object)
    return string if len(string) <= width else string[:width-len(ellipsis)] + ellipsis

def mapt(function: callable, *sequences) -> tuple:
    """`map`, with the result as a tuple."""
    return tuple(map(function, *sequences))

def mapl(function: callable, *sequences) -> list:
    """`map`, with the result as a list."""
    return list(map(function, *sequences))


"""Utility functions:"""

def cover(*integers) -> range:
    """A `range` that covers all the given integers, and any in between them.
    cover(lo, hi) is an inclusive (or closed) range, equal to range(lo, hi + 1).
    The same range results from cover(hi, lo) or cover([hi, lo])."""
    if len(integers) == 1: integers = the(integers)
    return range(min(integers), max(integers) + 1)

def the(sequence):
    """Return the one item in a sequence. Raise error if not exactly one."""
    for i, item in enumerate(sequence, 1):
        if i > 1: raise ValueError(f"'Expected exactly one item in the sequence.")
    return item

def intersection(sets: Sequence[set[T]]) -> set[T]:
    """Intersection of several sets; error if no sets"""
    first, *rest = sets
    return first.intersection(*rest)

flatten = chain.from_iterable


"""Points in Space"""

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


"""Points on a Grid"""

class Grid(dict):
    def __init__(self, grid=(), directions=directions4, skip: Tuple[any] = (), default: any = KeyError):
        super().__init__()
        self.directions = directions
        self.default = default
        self.update({(x, y): val
                     for y, row in enumerate(grid)
                     for x, val in enumerate(row)
                     if val not in skip})

    def __missing__(self, point):
        """If asked for a point off the grid, either return default or raise error."""
        if self.default is KeyError:
            raise KeyError(point)
        return self.default

    def neighbors(self, point: Point) -> List[Point]:
        """Points on the grid that neighbor `point`."""
        return [add(point, d) for d in self.directions
                if add(point, d) in self]

    def neighbor_contents(self, point: Point) -> Iterable:
        """The contents of the neighboring points."""
        return (self[p] for p in self.neighbors(point))

    def to_rows(self, xrange=None, yrange=None) -> List[List[any]]:
        """The contents of the grid, as a rectangular list of lists.
           You can define a window with an xrange and yrange; or they default to the whole grid."""
        xrange = xrange or cover(Xs(self))
        yrange = yrange or cover(Ys(self))
        default = " " if self.default is KeyError else self.default
        return [[self.get((x, y), default) for x in xrange]
                for y in yrange]

    def print(self, sep='', xrange=None, yrange=None):
        """Print a representation of the grid."""
        for row in self.to_rows(xrange, yrange):
            print(*row, sep=sep)
