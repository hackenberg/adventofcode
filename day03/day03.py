from functools import reduce


def p1(f):
    data = f.read().split('\n')[:-1]
    return sum(map(priority, map(find_common_item, map(split_backpack, data))))


def p2(f):
    data = f.read().split('\n')[:-1]
    def group(data):
        for i in range(0, len(data) - 2, 3):
            yield data[i], data[i+1], data[i+2]

    return sum(map(priority, map(find_common_item, group(data))))


def find_common_item(compartments):
    intersection = reduce(set.intersection, map(set, compartments))
    assert len(intersection) == 1
    return ''.join(intersection)


def split_backpack(items):
    length = len(items)
    assert length % 2 == 0
    return items[:length//2], items[length//2:]


def priority(item):
    ascii_offset = 38 if item.isupper() else 96
    return ord(item) - ascii_offset
