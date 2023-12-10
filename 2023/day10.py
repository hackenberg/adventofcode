from utils import *

from abc import ABC, abstractmethod

S = (0, 2)


class SearchProblem:
    def __init__(self, initial=None, **kwargs):
        self.__dict__.update(initial=initial, **kwargs)

    def actions(self, state):        raise NotImplementedError
    def result(self, state, action): return action  # Simplest case: action is result state


class GridProblem(SearchProblem):
    def actions(self, loc):       return self.grid.neighbors(loc)
    def result(self, loc1, loc2): return loc2


class PathfindingProblem(GridProblem):
    def actions(self, loc):
        return [d for d in (North, South, East, West) if self.is_connected(loc, d)]

    def is_connected(self, loc, direction) -> bool:
        loc2 = self.grid[add(loc, direction)]
        match direction:
            case (0, -1): return loc2 in ("|", "7", "F")
            case (0, 1): return loc2 in ("|", "L", "J")
            case (1, 0): return loc2 in ("-", "J", "7")
            case (-1, 0): return loc2 in ("-", "L", "F")


class Node:
    def __init__(self, state, path_cost=0):
        self.state = state
        self.path_cost = path_cost

    def __repr__(self): return f"Node({self.state}, path_cost={self.path_cost})"


def expand(problem: SearchProblem, node: Node):
    """Expand a node, generating all possible successors."""
    s = node.state
    for action in problem.actions(s):
        s2 = problem.result(s, action)
        cost = node.path_cost + 1
        yield Node(s2, cost)


def p1(text: str) -> any:
    in1 = parse(text)
    grid = Grid(in1, skip=(".",), default=".")
    initial = the(loc for loc in grid if grid[loc] == "S")
    pipes = PathfindingProblem(initial=initial, grid=grid)

    node = Node(pipes.initial)
    print(node)
    for n in expand(pipes, node):
        print(n)

    #import IPython; IPython.embed(colors="neutral")
    #import ipdb; ipdb.set_trace()


def p2(text: str) -> any:
    in2 = parse(text)
