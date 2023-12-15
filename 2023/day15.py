import re

from utils import *


def HASH(s: str, cur: int = 0) -> int:
    if not s: return cur
    c, *s = s
    return HASH(s, cur=((cur + ord(c)) * 17) % 256)


def p1(text: str) -> any:
    in1 = parse(text, str, lambda s: s.split(","))
    return sum(HASH(s) for s in in1)


class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

    def __eq__(self, other):
        return self.label == other.label


def focusing_power(box: int, slot: int, focal_length: int):
    return (box + 1) * slot * focal_length


def p2(text: str) -> any:
    in2 = parse(text, str, lambda s: s.split(","))
    hashmap = defaultdict(list)

    for step in in2:
        label, op, foc = re.split(r"(-|=)", step)
        h = HASH(label)
        match op:
            case "-": hashmap[h] = [lens for lens in hashmap[h] if lens.label != label]
            case "=":
                lens = Lens(label, int(foc))
                if lens in hashmap[h]:
                    hashmap[h][hashmap[h].index(lens)] = lens
                else:
                    hashmap[h].append(lens)

    total = 0
    for box, lenses in hashmap.items():
        for i, lens in enumerate(lenses):
            total += focusing_power(box, i+1, lens.focal_length)

    return total
