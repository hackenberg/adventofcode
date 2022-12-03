#!/usr/bin/env python3


def part_1(data):
    return sum(map(priority, map(find_common_item, data)))


def part_2(data):
    # TODO
    pass


def find_common_item(items):
    comp1, comp2 = split_backpack(items)
    intersection = set(comp1) & set(comp2)
    assert len(intersection) == 1
    return ''.join(intersection)


def split_backpack(items):
    length = len(items)
    assert length % 2 == 0
    return items[:length//2], items[length//2:]


def priority(item):
    ascii_offset = 38 if item.isupper() else 96
    return ord(item) - ascii_offset


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')[:-1]
    return data


if __name__ == '__main__':
    data = parse_input()
    print(f'Part 1: {part_1(data)}')
    print(f'Part 2: {part_2(data)}')
