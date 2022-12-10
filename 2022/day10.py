#import IPython; IPython.embed(colors="neutral")
#import ipdb; ipdb.set_trace()


def p1(f):
    instructions = f.read().splitlines()
    args = [1] + [0] * (len(instructions) * 2)
    cycle = 0

    for instr in instructions:
        match instr.split():
            case ["addx", arg]:
                cycle += 2
                args[cycle] = int(arg)
            case ["noop"]:
                cycle += 1
            case other:
                assert False

    signal_strength = lambda c: c * sum(args[:c])
    return sum(signal_strength(c) for c in [20, 60, 100, 140, 180, 220])


def p2(f):
    instructions = f.read().splitlines()
    args = [1] + [0] * (len(instructions) * 2)
    cycle = 0

    for instr in instructions:
        match instr.split():
            case ["addx", arg]:
                cycle += 2
                args[cycle] = int(arg)
            case ["noop"]:
                cycle += 1
            case other:
                assert False

    sprite = lambda c: sum(args[:c])

    for c in range(240):
        if c % 40 == 0:
            print()

        s = sprite(c + 1)

        if (c % 40) >= s-1 and (c % 40) <= s+1:
            print("#", end="")
        else:
            print(".", end="")

    print()
