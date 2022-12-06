#!/usr/bin/env python3


def part_1(data):
    for i in range(3, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i


def part_2(data):
    # TODO
    pass


def parse_input():
    with open(0) as stdin:
        data = stdin.read()
    return data


if __name__ == '__main__':
    data = parse_input()
    print(f'Part 1: {part_1(data)}')
    print(f'Part 2: {part_2(data)}')
