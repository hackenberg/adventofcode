import re


def manhattan_distance(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return abs(x0 - x1) + abs(y0 - y1)


def p1(f):
    print("NOTE: var t has to be adjusted for sample or real input")
    lines = f.read().splitlines()
    sensors = dict()
    beacons = set()
    row = set()
    t = 2000000

    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        r = manhattan_distance((sx, sy), (bx, by))
        if sy - r <= t <= sy + r:
            sensors[sx, sy] = r
        if by == t:
            beacons.add(bx)

    for s, r in sensors.items():
        sx, sy = s
        rx = r - abs(t - sy)
        for x in range(sx - rx, sx + rx + 1):
            row.add(x)

    row.difference_update(beacons)
    return len(row)


def p2(f):
    print("NOTE: var t has to be adjusted for sample or real input")
    lines = f.read().splitlines()
    sensors = dict()
    t = 4000000
    #t = 20

    for line in lines:
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        sensors[(sx, sy)] = manhattan_distance((sx, sy), (bx, by))

    def check(*p):
        px, py = p
        if px < 0 or px > t or py < 0 or py > t:
            return

        c = [s for s, r in sensors.items() if manhattan_distance(s, p) <= r]

        if len(c) <= 0:
            return px * 4000000 + py

    for s, r in sensors.items():
        sx, sy = s
        for i, y in enumerate(range(sy-r-1, sy+1)):
            a = check(sx-i, y)
            if a: return a
            a = check(sx+i, y)
            if a: return a
        for i, y in enumerate(range(sy+1, sy+r+2)):
            a = check(sx-r+i, y)
            if a: return a
            a = check(sx+r-i, y)
            if a: return a
