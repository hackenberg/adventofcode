from collections import defaultdict, deque, namedtuple
from math        import prod
from utils       import *

pattern = re.compile(r"(\d+) (red|green|blue)")


def p1(text: str) -> any:
    in1 = parse(text)
    limit = {"red": 12, "green": 13, "blue": 14}
    ans = 0
    for i, line in enumerate(in1):
        for amount, color in pattern.findall(line):
            if int(amount) > limit[color]:
                break
        else:
            ans += i + 1
    return ans


def p2(text: str) -> any:
    in2 = parse(text)
    ans = 0
    for line in in2:
        minimum_set = {"red": 0, "green": 0, "blue": 0}
        for amount, color in pattern.findall(line):
            minimum_set[color] = max(minimum_set[color], int(amount))
        ans += prod(minimum_set.values())
    return ans
