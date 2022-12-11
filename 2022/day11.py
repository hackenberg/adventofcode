import math
from collections import deque


class Monkey:
    def __init__(self, text):
        lines = text.splitlines()
        self.inspected = 0
        self.name = lines[0][:-1]
        for line in lines[1:]:
            match line.strip().split(": "):
                case ["Starting items", items]:
                    self.items = deque([int(s) for s in items.split(", ")])
                case ["Operation", operation]:
                    self.operation = eval(f"lambda old: {operation.split('=')[1]}")
                case ["Test", test]:
                    self.divisor = int(test.split()[-1])
                case ["If true", result]:
                    self.test_true = int(test.split()[-1])
                case ["If false", result]:
                    self.test_false = int(test.split()[-1])
                case other:
                    assert False

    def test(self, x):
        if x % self.divisor == 0:
            return self.test_true
        else:
            return self.test_false

    def inspect_next(self):
        self.inspected += 1
        item = self.items.popleft()
        item = self.operation(item)
        item = math.trunc(item / 3)
        return item, self.test(item)

    def __repr__(self):
        return f"{self.name}"


def p1(f):
    monkeys = [Monkey(text) for text in f.read().split("\n\n")]

    for i in range(20):
        for monkey in monkeys:
            while monkey.items:
                item, target = monkey.inspect_next()
                monkeys[target].items.append(item)

    return math.prod(sorted([m.inspected for m in monkeys])[-2:])


class Monkey2(Monkey):
    def inspect_next(self, mod):
        self.inspected += 1
        item = self.items.popleft()
        item = self.operation(item) % mod
        return item, self.test(item)


def p2(f):
    monkeys = [Monkey2(text) for text in f.read().split("\n\n")]
    mod = math.prod(m.divisor for m in monkeys)

    for i in range(10000):
        for monkey in monkeys:
            while monkey.items:
                item, target = monkey.inspect_next(mod)
                monkeys[target].items.append(item)

    return math.prod(sorted([m.inspected for m in monkeys])[-2:])
