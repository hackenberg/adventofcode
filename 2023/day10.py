from utils import *


class SearchProblem:
    def __init__(self, initial=None, **kwargs):
        self.__dict__.update(initial=initial, **kwargs)

    def actions(self, state):        raise NotImplementedError
    def result(self, state, action): return action  # Simplest case: action is result state


class GridProblem(SearchProblem):
    def actions(self, loc):       return self.grid.neighbors(loc)


class PipeMazeProblem(GridProblem):
    def actions(self, loc):
        return [add(loc, direction)
                for direction in (North, South, East, West)
                if self.is_connected(loc, direction)]

    def is_connected(self, loc, direction) -> bool:
        loc2 = self.grid[add(loc, direction)]
        match direction:
            case (0, -1): return loc2 in ("|", "7", "F")
            case (0, 1):  return loc2 in ("|", "L", "J")
            case (1, 0):  return loc2 in ("-", "J", "7")
            case (-1, 0): return loc2 in ("-", "L", "F")


class Node:
    def __init__(self, state, path_cost=0):
        self.state = state
        self.path_cost = path_cost

    def __repr__(self):      return f"Node({self.state}, path_cost={self.path_cost})"
    def __lt__(self, other): return self.path_cost < other.path_cost


def expand(problem: SearchProblem, node: Node):
    """Expand a node, generating all possible children."""
    s = node.state
    for action in problem.actions(s):
        s2 = problem.result(s, action)
        cost = node.path_cost + 1
        yield Node(s2, cost)


def breadth_first_search(problem: SearchProblem):
    """Enumerate the problem space."""
    frontier = {Node(problem.initial)}
    reached = {}

    while frontier:
        node = frontier.pop()
        if (node.state in reached) and reached[node.state] < node:
            continue
        reached[node.state] = node
        for child in expand(problem, node):
            frontier.add(child)

    return reached.values()


def p1(text: str) -> any:
    in1 = parse(text)
    grid = Grid(in1, skip=(".",), default=".")
    initial = the(loc for loc in grid if grid[loc] == "S")

    pipes = PipeMazeProblem(initial=initial, grid=grid)
    nodes = breadth_first_search(pipes)

    return max(node.path_cost for node in nodes)


def p2(text: str) -> any:
    in2 = parse(text)
    #import IPython; IPython.embed(colors="neutral")
    #import ipdb; ipdb.set_trace()
