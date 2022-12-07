def p1(f):
    def is_valid(line):
        r, char, pwd = line.split()
        lb, ub = map(int, r.split("-"))
        char = char.replace(":", "")
        occurences = len([c for c in pwd if c == char])
        return occurences >= lb and occurences <= ub

    return sum(map(is_valid, f.read().splitlines()))


def p2(f):
    def is_valid(line):
        r, char, pwd = line.split()
        lb, ub = map(int, r.split("-"))
        char = char.replace(":", "")
        return (pwd[lb-1] == char) ^ (pwd[ub-1] == char)

    return sum(map(is_valid, f.read().splitlines()))
