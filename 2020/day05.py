def p1(f):
    lines = f.read().splitlines()
    return max(map(seat_id, lines))


def seat_id(s):
    row = int(s[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(s[7:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col


def p2(f):
    lines = f.read().splitlines()
    ids = sorted(map(seat_id, lines))
    for i in range(1, len(ids)):
        if ids[i-1] + 2 == ids[i]:
            return ids[i] - 1
