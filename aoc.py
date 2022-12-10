from functools import reduce


def mult(iterable):
    return reduce(lambda x, y: x * y, iterable)


def add(*tuples):
    return tuple(map(sum, zip(*tuples)))
