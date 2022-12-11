import math
import operator
import re
from collections import deque
#import ipdb; ipdb.set_trace()


class Monkey:
    def __init__(self, lines):
        self.inspected = 0
        self.name = lines[0][:-1]
        for line in lines[1:]:
            match line.strip().split(":"):
                case ["Starting items", items]:
                    self.items = deque([int(s.strip()) for s in items.split(",")])
                case ["Operation", operation]:
                    r = re.search(r"new = old (.) (\S+)", operation)
                    match r.group(1):
                        case "+": op = operator.add
                        case "*": op = operator.mul
                        case other: assert False
                    match r.group(2):
                        case "old": self.operation = lambda n: op(n, n)
                        case val: self.operation = lambda n: op(n, int(val))
                case ["Test", test]:
                    divisor = int(test.replace(" divisible by ", ""))
                    self.test = lambda n: n % divisor == 0
                case ["If true", test_true]:
                    self.test_true = int(test_true.replace(" throw to monkey ", ""))
                case ["If false", test_false]:
                    self.test_false = int(test_false.replace(" throw to monkey ", ""))
                case other:
                    assert False

    def __repr__(self):
        return f"{self.name}"

    def inspect_next(self):
        self.inspected += 1
        item = self.items.popleft()
        item = self.operation(item)
        item = math.trunc(item / 3)
        target = self.test_true if self.test(item) else self.test_false
        return item, target


def p1(f):
    monkeys = list(map(Monkey, [s.splitlines() for s in f.read().split("\n\n")]))

    for i in range(20):
        for monkey in monkeys:
            while monkey.items:
                item, target = monkey.inspect_next()
                monkeys[target].items.append(item)

        #print(f"== After round {i+1} ==")
        #for monkey in monkeys:
        #    print(f"{monkey.name}: {monkey.items}")
        #for monkey in monkeys:
        #    print(f"{monkey.name} inspected items {monkey.inspected} times.")

    return math.prod(list(sorted([m.inspected for m in monkeys]))[-2:])


def p2(f):
    pass
