from functools import reduce


def add(*tuples):
    return tuple(map(sum, zip(*tuples)))
