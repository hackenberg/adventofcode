# start: Di 03 Dez 2024 10:09:49 CET
# p1: Di 03 Dez 2024 10:27:27 CET
# p2: Di 03 Dez 2024 11:16:42 CET

from utils import *


def p1(text: str) -> any:
    m = re.findall(r"mul\((\d\d?\d?),(\d\d?\d?)\)", text)
    return sum(int(x) * int(y) for x, y in m)


def p2(text: str) -> any:
    pattern = re.compile(r"mul\((\d\d?\d?),(\d\d?\d?)\)|do\(\)|don't\(\)")
    do = True
    solution = 0

    for m in pattern.finditer(text):
        if m.group().startswith("don"):
            do = False
        elif m.group().startswith("do"):
            do = True
        elif do:
            x, y = map(int, re.findall("\d+", m.group()))
            solution += x * y
        else:
            pass

    return solution
