from collections import defaultdict, deque
from utils       import *


def p1(text):
    in1 = parse(text, int, sections=lambda s: s.split(","))
    total = defaultdict(int)
    minimum = (0, 1000)
    for i in range(min(in1), max(in1) + 1):
        total[i] = 0
        for x in in1:
            total[i] += abs(i - x)
        if `

    return min(total.values())


