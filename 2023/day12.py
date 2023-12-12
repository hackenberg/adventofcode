from utils import *

DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"


class GraphSearchProblem:
    def __init__(self, initial=None, goal=None, **kwargs):
        self.__dict__.update(initial=initial, goal=goal, **kwargs)

    def actions(self):
        return DAMAGED, OPERATIONAL

    def result(self, state, action):
        return state.replace(UNKNOWN, action, 1)


def expand(problem, state):
    for action in problem.actions():
        yield problem.result(state, action)


def check_arrangement(chars, nums):
    return tuple(len(cs) for cs in chars.split(OPERATIONAL) if cs.count(DAMAGED)) == nums


def search(problem):
    state = problem.initial
    frontier = {state}
    candidates = set()
    while frontier:
        state = frontier.pop()
        for child in expand(problem, state):
            if child.count(DAMAGED) > sum(problem.goal):
                continue
            if child.count(DAMAGED) + child.count(UNKNOWN) < sum(problem.goal):
                continue
            if UNKNOWN in child:
                frontier.add(child)
            else:
                candidates.add(child)

    return [solution for solution in candidates if check_arrangement(solution, problem.goal)]


def parse_in1(line: str) -> tuple[str, tuple[int, ...]]:
    chars, nums = line.split()
    return chars, mapt(int, nums.split(","))


def p1(text: str) -> any:
    in1 = parse(text, parse_in1)
    ans = 0
    for chars, nums in in1:
        problem = GraphSearchProblem(chars, nums)
        solutions = search(problem)
        ans += len(solutions)
    return ans


def p2(text: str) -> any:
    in2 = parse(text)
    #show_items("Parsed input", in2, 5)
