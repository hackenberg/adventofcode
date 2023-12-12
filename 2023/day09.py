from utils import *


def predict_next(history: Sequence[int]) -> int:
    if all(x == 0 for x in history):
        return 0
    differences = [y - x for x, y in zip(history, history[1:])]
    return history[-1] + predict_next(differences)


def p1(text: str) -> any:
    in1 = parse(text, ints)
    return sum(map(predict_next, in1))


def predict_previous(history: Sequence[int]) -> int:
    if all(x == 0 for x in history):
        return 0
    differences = [y - x for x, y in zip(history, history[1:])]
    return history[0] - predict_previous(differences)


def p2(text: str) -> any:
    in2 = parse(text, ints)
    return sum(map(predict_previous, in2))
