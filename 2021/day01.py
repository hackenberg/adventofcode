def p1(f):
    lines = f.read().splitlines()
    #import IPython; IPython.embed(colors="neutral")
    #import ipdb; ipdb.set_trace()
    xs = [int(l) for l in lines]
    return sum(x < y for x, y in zip(xs, xs[1:]))


def p2(f):
    lines = f.read().splitlines()
    xs = [int(l) for l in lines]
    ts = [sum(t) for t in zip(xs, xs[1:], xs[2:])]
    return sum(a < b for a, b in zip(ts, ts[1:]))
