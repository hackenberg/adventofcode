from collections import defaultdict, deque
from utils       import *


def p1(text):
    in1 = parse(text, int, sections=lambda s: s.split(","))
    fishes = deque([0] * 9)
    for n in in1:
        fishes[n] += 1

    for day in range(80):
        ready = fishes.popleft()
        fishes.append(ready)
        fishes[6] += ready

    return sum(fishes)


def p2(text):
    in1 = parse(text, int, sections=lambda s: s.split(","))
    fishes = deque([0] * 9)
    for n in in1:
        fishes[n] += 1

    for day in range(256):
        ready = fishes.popleft()
        fishes.append(ready)
        fishes[6] += ready

    return sum(fishes)