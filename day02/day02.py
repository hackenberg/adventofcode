#!/usr/bin/env python3

ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSORS = ['C', 'Z']


class Choice:
    def __init__(self, beats, draws, loses):
        self.beats = beats
        self.draws = draws
        self.loses = loses

    def versus(self, opponent):
        if opponent in self.beats:
            return 6
        if opponent in self.draws:
            return 3
        if opponent in self.loses:
            return 0


class Rock(Choice):
    value = 1
    def __init__(self):
        super().__init__(SCISSORS, ROCK, PAPER)


class Paper(Choice):
    value = 2
    def __init__(self):
        super().__init__(ROCK, PAPER, SCISSORS)


class Scissors(Choice):
    value = 3
    def __init__(self):
        super().__init__(PAPER, SCISSORS, ROCK)


CHOICES = {
    'A': Rock(), 'X': Rock(),
    'B': Paper(), 'Y': Paper(),
    'C': Scissors(), 'Z': Scissors(),
}


def part_1():
    data = parse_input()
    score = 0
    for row in data:
        me = CHOICES[row[1]]
        score += me.versus(row[0])
        score += me.value
    return score


def part_2():
    data = parse_input()
    # TODO
    return None


def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')[:-1]
    return map(lambda s: s.split(), data)


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
