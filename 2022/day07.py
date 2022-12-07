def p1(f):
    dirs, total_sizes = parse_input(f)
    return sum([size for size in total_sizes if size <= 100000])


def p2(f):
    dirs, total_sizes = parse_input(f)
    root_size = max(total_sizes)
    required_extra_space = (root_size + 30000000) - 70000000
    return min([size for size in total_sizes if size >= required_extra_space])


def parse_input(f):
    cwd = ["/"]
    dirs = {"/": []}

    for line in f.read().splitlines():
        if line.startswith("$ cd "):
            arg = line.replace("$ cd ", "")
            if arg == "..":
                cwd.pop()
            elif arg == "/":
                continue
            else:
                cwd.append(f"{arg}/")
                dirs["".join(cwd)] = []
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        else:
            size, _ = line.split()
            dirs["".join(cwd)].append(int(size))

    total_sizes = []
    for d in dirs:
        d_size = 0  # lol
        for key, value in dirs.items():
            if key.startswith(d):
                d_size += sum(value)
        total_sizes.append(d_size)

    return dirs, total_sizes
