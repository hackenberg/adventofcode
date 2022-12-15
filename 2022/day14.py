from collections import defaultdict


def p1(f):
    lines = f.read().splitlines()
    grid = defaultdict(int)
    max_depth = 0

    for line in lines:
        points = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        for i in range(0, len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i+1]
            for y in range(min(y0, y1), max(y0, y1) + 1):
                max_depth = max(y, max_depth)
                for x in range(min(x0, x1), max(x0, x1) + 1):
                    grid[(x, y)] = -1

    #print_grid(grid, 450, 550, 180)

    i = 0
    while drop_sand(grid, max_depth):
        i += 1

    #print_grid(grid, 450, 550, 180)

    return i


def drop_sand(grid, max_depth, point=(500, 0)):
    x, y = point

    if y >= max_depth:
        return False

    if not grid[(x+0, y+1)]:
        return drop_sand(grid, max_depth, (x, y+1))
    elif not grid[(x-1, y+1)]:
        return drop_sand(grid, max_depth, (x-1, y+1))
    elif not grid[(x+1, y+1)]:
        return drop_sand(grid, max_depth, (x+1, y+1))

    grid[point] = +1
    return True


def print_grid(grid, x0=494, x1=504, depth=10):
    for y in range(0, depth):
        for x in range(x0, x1):
            if grid[(x, y)]:
                print("#" if grid[(x, y)] < 0 else "o", end = "")
            else:
                print(".", end="")
        print()
    print()


def p2(f):
    lines = f.read().splitlines()
    grid = defaultdict(int)
    max_depth = 0

    for line in lines:
        points = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        for i in range(0, len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i+1]
            for y in range(min(y0, y1), max(y0, y1) + 1):
                max_depth = max(y, max_depth)
                for x in range(min(x0, x1), max(x0, x1) + 1):
                    grid[(x, y)] = -1

    max_depth += 2
    for i in range(0, 1000):
        grid[(i, max_depth)] = -1

    #print_grid(grid, 450, 550, 180)

    i = 1
    while drop_sand(grid, max_depth) and not grid[(500, 0)]:
        i += 1

    #print_grid(grid, 300, 700, 180)

    return i
