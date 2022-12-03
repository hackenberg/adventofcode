#!/usr/bin/env python3
from functools import reduce


def part_1(data):
    return sum(map(priority, map(find_common_item, map(split_backpack, data))))


def part_2(data):
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


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')[:-1]
    return data


if __name__ == '__main__':
    data = parse_input()
    print(f'Part 1: {part_1(data)}')
    print(f'Part 2: {part_2(data)}')
