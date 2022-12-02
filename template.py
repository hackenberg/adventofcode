#!/usr/bin/env python3


def part_1():
    data = parse_input()
    return None


def part_2():
    data = parse_input()
    return None


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    return data


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
