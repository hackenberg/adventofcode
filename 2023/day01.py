from utils import *


def p1(text: str) -> any:
    in1 = parse(text, ints)
    return sum(map(first_and_last, map(lambda x: "".join(map(str, x)), in1)))


def first_and_last(s: str) -> int:
    return int(s[0] + s[-1])


def p2(text: str) -> any:
    in2 = parse(text)
    r = r"[0-9]|one|two|three|four|five|six|seven|eight|nine"
    pattern = re.compile(rf"({r}).*({r})")
    total = 0
    for line in in2:
        match = pattern.search(line)
        if match:
            first, last = match.groups()
        else:
            match = re.search(r"([0-9]|one|two|three|four|five|six|seven|eight|nine)", line)
            first = the(match.groups())
            last = the(match.groups())
        total += int(parse_digit(first) + parse_digit(last))
    return total


def parse_digit(s: str) -> str:
    match s:
        case "one": return "1"
        case "two": return "2"
        case "three": return "3"
        case "four": return "4"
        case "five": return "5"
        case "six": return "6"
        case "seven": return "7"
        case "eight": return "8"
        case "nine": return "9"
        case _: return s
