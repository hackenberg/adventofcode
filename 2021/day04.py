from collections import defaultdict, deque
from utils       import *

B = 5
Board = Tuple[int]  # B * B ints
Line = list[int]  # B ints


def p1(text):
    numbers, *boards = parse(text, ints, paragraphs)
    drawn = set()
    for num in numbers:
        drawn.add(num)
        winners = check(boards, drawn, num)


def check(boards, drawn, num):
    [b for b in boards
     if num in boards and any(filled)]

    #import IPython; IPython.embed(colors="neutral")
    #import ipdb; ipdb.set_trace()

#     for n in numbers:
#         print(f"n={n}")
#         for b in boards:
#             print(f"b={b}")
#             for y in range(B):
#                 for x in range(B):
#                     if b[y][x] == n:
#                         b[y][x] = 0
#             if check(b):
#                 for r in b:
#                     print(r)
#
#
# def check(board):
#     for i in range(0, B**2, B):
#         if sum(row) == 0:
#             return True
#     for i in range(len(board[0])):
#         col = [r[i] for r in board]
#         if sum(col) == 0:
#             return True


def parse_input(lines):
    numbers = lines[0]
    boards = []
    for i in range(2, len(lines), 6):
        rows = [[int(n) for n in l.split()] for l in lines[i:i+5]]
        columns = [
            [r[0] for r in rows],
            [r[1] for r in rows],
            [r[2] for r in rows],
            [r[3] for r in rows],
            [r[4] for r in rows],
        ]
        boards.append(rows + columns)
    return numbers, boards


# def p2(f):
#     pass