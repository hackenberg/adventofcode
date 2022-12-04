#!/usr/bin/env python3


def part_1(data):
    return sum([fully_contains(r) for r in map(split_row, data)])


def split_row(row):
    return [s.split('-') for s in row.split(',')]


def fully_contains(row):
    sl = int(row[0][0]) # start of left range
    el = int(row[0][1]) # end of left range
    sr = int(row[1][0]) # start of right range
    er = int(row[1][1]) # end of right range
    return (sl <= sr and el >= er) or (sl >= sr and el <= er)


def part_2(data):
    pass


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')[:-1]
    return data


if __name__ == '__main__':
    data = parse_input()
    print(f'Part 1: {part_1(data)}')
    print(f'Part 2: {part_2(data)}')
