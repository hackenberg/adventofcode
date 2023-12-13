from utils import *

DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"


def expand(state):
    for action in (DAMAGED, OPERATIONAL):
        yield state.replace(UNKNOWN, action, 1)


def check_arrangement(chars, nums):
    return tuple(len(cs) for cs in chars.split(OPERATIONAL) if cs.count(DAMAGED)) == nums


def search(chars, nums):
    state = chars
    frontier = {state}
    candidates = set()
    while frontier:
        state = frontier.pop()
        for child in expand(state):
            if child.count(DAMAGED) > sum(nums):
                continue
            if child.count(DAMAGED) + child.count(UNKNOWN) < sum(nums):
                continue
            if UNKNOWN in child:
                frontier.add(child)
            else:
                candidates.add(child)

    return [solution for solution in candidates if check_arrangement(solution, nums)]


def parse_in1(line: str) -> tuple[str, tuple[int, ...]]:
    chars, nums = line.split()
    return chars, mapt(int, nums.split(","))


def p1(text: str) -> any:
    in1 = parse(text, parse_in1)
    ans = 0
    for chars, nums in in1:
        solutions = search(chars, nums)
        ans += len(solutions)
    return ans


def p2(text: str) -> any:
    in2 = parse(text)
    #show_items("Parsed input", in2, 5)
