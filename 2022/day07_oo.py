from collections import defaultdict


class Node:
    def __init__(self, parent, dirname):
        self.parent = parent
        self.dirname = dirname

    def __repr__(self):
        return f"{self.parent.__repr__()}{self.dirname}/"

    @property
    def parents(self):
        return [self.parent, *self.parent.parents]

    def resolve(self, newdir):
        if newdir == "..":
            return self.parent
        return Node(self, newdir)


class Root(Node):
    def __init__(self):
        return super().__init__(None, "/")

    def __repr__(self):
        return "/"

    @property
    def parents(self):
        return []


def parse_dirs(f):
    cwd = Root()
    dirs = defaultdict(int)

    for line in f.read().splitlines()[1:]:
        if line.startswith("$ cd "):
            newdir = line.replace("$ cd ", "")
            cwd = cwd.resolve(newdir)

        elif line.split()[0].isdigit():
            size = int(line.split()[0])
            for d in [cwd, *cwd.parents]:
                dirs[str(d)] += size

    return dirs


def p1(f):
    dirs = parse_dirs(f)
    return sum(n for n in dirs.values() if n <= 100000)


def p2(f):
    dirs = parse_dirs(f)
    return min(n for n in dirs.values() if dirs["/"] - n <= 70000000 - 30000000)
