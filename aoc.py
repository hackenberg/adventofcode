from functools import reduce


def mult(iterable):
    return reduce(lambda x, y: x * y, iterable)
