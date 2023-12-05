from utils import *


def to_location(seed: int, maps: list[tuple[tuple[int, int, int]]]) -> int:
    for m in maps:
        for line in m:
            dst, src, r = line
            if seed in range(src, src+r):
                seed += dst - src
                break
    return seed


def p1(text: str) -> any:
    in1 = parse(text, ints, paragraphs)
    seeds = in1[0]
    maps = [tuple(zip(p[0::3], p[1::3], p[2::3])) for p in in1[1:]]
    return min(to_location(s, maps) for s in seeds)


def to_seed(location: int, maps: list[tuple[tuple[int, int, int]]]) -> int:
    for m in reversed(maps):
        for line in m:
            dst, src, r = line
            if location - (dst - src) in range(src, src+r):
                location -= dst - src
                break
    return location


def p2(text: str) -> any:
    in1 = parse(text, ints, paragraphs)
    seed_ranges = tuple(zip(in1[0][0::2], in1[0][1::2]))
    maps = [tuple(zip(p[0::3], p[1::3], p[2::3])) for p in in1[1:]]
    for location in count():
        seed = to_seed(location, maps)
        for start, length in seed_ranges:
            if start <= seed < (start + length):
                return location
