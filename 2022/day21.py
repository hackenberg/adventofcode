from collections import defaultdict, deque, namedtuple
from math        import prod
from operator    import add, floordiv, mul, sub, truediv
from utils       import *

import sympy


class MonkeyOperation():
    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
        "=": sympy.Eq,
    }

    def __init__(self, lchild, op, rchild):
        self.lchild = lchild
        self.op = op
        self.rchild = rchild

    def resolve(self, monkeys):
        lval = monkeys[self.lchild].resolve(monkeys)
        rval = monkeys[self.rchild].resolve(monkeys)
        print(lval, rval)
        return MonkeyOperation.operators[self.op](lval, rval)

    def __repr__(self):
        return f"({self.lchild} {self.op} {self.rchild})"


class MonkeyValue():
    def __init__(self, val):
        self.val = val

    def resolve(self, monkeys):
        return self.val

    def __repr__(self):
        return f"({self.val})"


def p1(text: str) -> any:
    in1 = parse(text)
    monkeys = {}
    for line in in1:
        label, *job = line.replace(":", "").split()
        if len(job) == 3:
            monkeys[label] = MonkeyOperation(*job)
        else:
            monkeys[label] = MonkeyValue(int(the(job)))
    
    return int(monkeys["root"].resolve(monkeys))


def p2(text: str) -> any:
    in1 = parse(text)
    monkeys = {}
    for line in in1:
        label, *job = line.replace(":", "").split()
        if label == "root":
            l, _, r = job
            monkeys["root"] = MonkeyOperation(l, "=", r)
        elif label == "humn":
            monkeys["humn"] = MonkeyValue(sympy.Symbol("humn"))
        elif len(job) == 3:
            monkeys[label] = MonkeyOperation(*job)
        else:
            monkeys[label] = MonkeyValue(*job)
    
    print(monkeys)
    return sympy.solve(monkeys["root"].resolve(monkeys))


def p3(text: str) -> any:
    in2 = parse(text)
    monkeys = {label: job for label, job in [line.split(": ") for line in in2]}
    pattern = re.compile(r"[a-z]{4}")

    def expand(job):
        ms = re.findall(pattern, job)
        if (not ms) or (len(ms) == 1 and ms[0] == "humn"):
            return job.replace("/", "//")
        for m in ms:
            if m == "humn":
                continue
            job = job.replace(m, f"({monkeys[m]})")
        return expand(job)

    lroot, _, rroot = monkeys["root"].split()

    lexpanded = expand(lroot)
    rexpanded = expand(rroot)

    if "humn" in lexpanded:
        solver = lambda x: eval(lexpanded.replace("humn", str(x)))
        target = eval(rexpanded)
    else:
        solver = lambda x: eval(rexpanded.replace("humn", str(x)))
        target = eval(lexpanded)

    # print(lexpanded)
    # print(rexpanded)

    # for i in range(100000):
    #     if i % 100 == 0: print(i)
    #     if target == solver(i):
    #         return i
    # return None

    return lexpanded, rexpanded


def p4(text: str) -> any:
    in2 = parse(text)
    monkeys = {}
    for line in in2:
        label, job = line.split(": ")
        op_or_val = job.split()

        if label == "root":
            lroot, _, rroot = op_or_val
            continue

        if len(op_or_val) == 3:
            monkeys[label] = MonkeyOperation(label, *op_or_val)
        else:
            monkeys[label] = MonkeyValue(label, *op_or_val)

    for label, job in monkeys.items():
        print(monkeys)
        simplified = job.simplify(monkeys)
        print(simplified)
        if simplified:
            monkeys[label] = simplified
    
    lexpanded, rexpanded = p3(text)

    if "humn" in lexpanded:
        solver = lambda x: monkeys[lroot].resolve(monkeys, humn=x)
        target = monkeys[rroot].resolve(monkeys)
    else:
        solver = lambda x: monkeys[rroot].resolve(monkeys, humn=x)
        target = monkeys[lroot].resolve(monkeys)

    print(target)

    for i in range(10**6):
        if i % 10**4 == 0: print(i)
        if target == solver(i):
            return i
