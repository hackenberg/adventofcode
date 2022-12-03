#!/usr/bin/env python3


def part_1():
    pass


def part_2():
    pass


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')[:-1]
    return data


if __name__ == '__main__':
    data = parse_input()
    print(f'Part 1: {part_1(data)}')
    print(f'Part 2: {part_2(data)}')
