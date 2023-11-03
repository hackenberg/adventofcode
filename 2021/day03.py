import operator


def p1(f):
    lines = f.read().splitlines()
    #import IPython; IPython.embed(colors="neutral")
    #import ipdb; ipdb.set_trace()

    gamma, epsilon = [], []
    for i in range(len(lines[0])):
        col = [l[i] for l in lines]
        gamma.append(max(col, key=col.count))
        epsilon.append(min(col, key=col.count))

    return int("".join(gamma), base=2) * int("".join(epsilon), base=2)


def p2(f):
    lines = f.read().splitlines()

    def f(lines, i=0, comp=operator.gt):
        if len(lines) <= 1:
            return lines

        zeroes = len([l[i] for l in lines if l[i] == "0"])
        ones = len([l[i] for l in lines if l[i] == "1"])

        if comp(zeroes, ones):
            discriminator = "0"
        else:
            discriminator = "1"

        return f([l for l in lines if l[i] == discriminator], i+1, comp)

    o2 = int("".join(f(lines)), base=2)
    co2 = int("".join(f(lines, comp=operator.le)), base=2)

    return o2 * co2
