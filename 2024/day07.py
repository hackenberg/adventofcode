from functools import reduce
from utils import *


def p1(text: str) -> any:
    in1 = parse(text, lambda s: s.split(": "))
    ans = 0
    for test_value, numbers in in1:
        test_value = int(test_value)
        ints = [int(n) for n in numbers.split()]
        operations = (operator.add, operator.mul)
        r = len(ints) - 1
        for ops in cross_product(operations, repeat=r):
            f = lambda a, b: b[0](a, b[1])
            val = reduce(f, zip(ops, ints[1:]), ints[0])
            if val == test_value:
                ans += test_value
                break
    return ans


def p2(text: str) -> any:
    in1 = parse(text, lambda s: s.split(": "), show=8)
    ans = 0
    for test_value, numbers in in1:
        test_value = int(test_value)
        ints = [int(n) for n in numbers.split()]
        concat = lambda a, b: int(str(a) + str(b))
        operations = (operator.add, operator.mul, concat)
        r = len(ints) - 1
        for ops in cross_product(operations, repeat=r):
            f = lambda a, b: b[0](a, b[1])
            val = reduce(f, zip(ops, ints[1:]), ints[0])
            if val == test_value:
                ans += test_value
                break
    return ans
