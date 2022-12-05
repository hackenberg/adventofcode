#!/usr/bin/env python3


def part_1(data):
    stacks, instructions = data
    for times, src, dest in instructions:
        for i in range(0, times):
            crate = stacks[src].pop()
            stacks[dest].append(crate)
    return get_message(stacks)


def part_2(data):
    stacks, instructions = data
    for times, src, dest in instructions:
        crates = popn(stacks[src], times)
        stacks[dest] += crates
    return get_message(stacks)


def get_message(stacks):
    return ''.join([s[-1] for s in stacks])


def popn(stack, n):
    buf = stack[-n:]
    del stack[-n:]
    return buf


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read()
    drawing, instructions = data.rstrip().split('\n\n')
    return parse_drawing(drawing), parse_instructions(instructions)


def parse_drawing(drawing):
    # Split into rows and remove indices
    rows = drawing.split('\n')[:-1]
    stacks = []
    for column in range(1, len(rows[0]), 4):
        # Parse column and remove whitespace
        crates = ''.join([row[column] for row in rows]).lstrip()
        stacks.append(list(crates[::-1]))
    return stacks


def parse_instructions(instructions):
    instructions = instructions.rstrip().split('\n')
    def parse_line(instr):
        instr = instr.replace('move ', '')
        instr = instr.replace('from ', '')
        instr = instr.replace('to ', '')
        instr = [int(i) for i in instr.split()]
        # Make life easier by using zero-based indexing
        instr[1] -= 1
        instr[2] -= 1
        return instr
    return [parse_line(line) for line in instructions]


if __name__ == '__main__':
    # Parse input twice because we are going to modify it in place
    print(f'Part 1: {part_1(parse_input())}')
    print(f'Part 2: {part_2(parse_input())}')
