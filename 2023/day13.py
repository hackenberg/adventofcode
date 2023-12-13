from utils import *


def is_symmetrical_around_index(seq: list[Sequence[str]], idx: int, offset: int = 0) -> bool:
    if idx - offset <= 0 or idx + offset >= len(seq):
        return True
    left = seq[idx-offset-1]
    right = seq[idx+offset]
    return left == right and is_symmetrical_around_index(seq, idx, offset+1)


def p1(text: str) -> any:
    in1 = parse(text, lines, paragraphs)
    ans = 0
    for grid in map(Grid, in1):
        rows = grid.to_rows()
        cols = T(rows)
        for y in range(1, max(Xs(grid))):
            if is_symmetrical_around_index(cols, y):
                ans += y
        for x in range(1, max(Ys(grid))):
            if is_symmetrical_around_index(rows, x):
                ans += 100*x
    return ans


def p2(text: str) -> any:
    in2 = parse(text)
    #show_items("Parsed input", in2, 10)
