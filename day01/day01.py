#!/usr/bin/env python3


def part_1():
    data = parse_input()
    max_calories = 0
    current_calories = 0

    for row in data:
        if not row:
            max_calories = max(max_calories, current_calories)
            current_calories = 0
            continue

        current_calories += int(row)

    return max_calories


def part_2():
    data = parse_input()
    inventory = []
    current_calories = 0

    for row in data:
        if not row:
            inventory.append(current_calories)
            current_calories = 0
            continue

        current_calories += int(row)

    inventory.sort(reverse=True)
    return sum(inventory[:3])


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')
    return data


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
