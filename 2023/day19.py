from utils import *

re_workflow = re.compile(r"(\w+){(.*)}")

Xmas = namedtuple("Xmas", "x, m, a, s")


def is_accepted(workflows, xmas, w1="in"):
    if w1 in ("A", "R"):
        return w1 == "A"

    for rule in workflows[w1].split(","):
        match rule.split(":"):
            case condition, w2:
                x, m, a, s = xmas  # declare variables for eval
                if eval(condition):
                    break
            case [w2]:
                continue

    return is_accepted(workflows, xmas, w2)


def p1(text: str) -> any:
    in1, in2 = parse(text, str, paragraphs, show=0)
    workflows = {k: v for k, v in re_workflow.findall(in1)}
    parts = tuple(Xmas(*ints(s)) for s in in2.splitlines())
    return sum(sum(xmas) for xmas in parts if is_accepted(workflows, xmas))
