from pathlib import Path
from typing  import Callable, Tuple, Union

import re

INPUT_DIR = Path(__file__).parent / "input"
YEAR = "2021"

lines = str.splitlines
def paragraphs(text: str) -> list[str]: return text.split("\n\n")


def parse(day_or_text, parser: Callable = str, sections: Callable = lines, sample: bool = False) -> tuple:
    text = get_text(day_or_text, sample)
    return mapt(parser, sections(text.rstrip()))


def get_text(day_or_text: Union[int, str], sample: bool = False) -> str:
    if isinstance(day_or_text, str):
        return day_or_text

    suffix = "_sample" if sample else ""
    input_file = INPUT_DIR / YEAR / f"day{day_or_text:02}{suffix}.txt"
    return input_file.read_text()


"""Functions that can be used as the parser argument:"""

def ints(text: str) -> Tuple[int]:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'-?[0-9]+', text))


"""Helper functions:"""

def mapt(function: Callable, *sequences) -> tuple:
    """`map`, with the result as a tuple."""
    return tuple(map(function, *sequences))

def mapl(function: Callable, *sequences) -> list:
    """`map`, with the result as a list."""
    return list(map(function, *sequences))


"""Utility functions:"""

def cover(*integers) -> range:
    """A `range` that covers all the given integers, and any in between them.
    cover(lo, hi) is an inclusive (or closed) range, equal to range(lo, hi + 1).
    The same range results from cover(hi, lo) or cover([hi, lo])."""
    if len(integers) == 1: integers = the(integers)
    return range(min(integers), max(integers) + 1)

def the(sequence) -> object:
    """Return the one item in a sequence. Raise error if not exactly one."""
    for i, item in enumerate(sequence, 1):
        if i > 1: raise ValueError(f"'Expected exactly one item in the sequence.")
    return item
