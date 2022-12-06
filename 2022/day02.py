from abc import ABC


class Choice(ABC):
    """A Choice is either Rock, Paper or Scissors."""
    def __init__(self, beats, draws, loses):
        self.beats = beats
        self.draws = draws
        self.loses = loses

    def versus(self, opponent):
        """Solution for Part 1"""
        assert opponent in ['A', 'B', 'C']
        if opponent in self.beats:
            return 6
        if opponent in self.draws:
            return 3
        if opponent in self.loses:
            return 0

    def fulfill_prediction(self, prediction):
        """Solution for Part 2"""
        assert prediction in ['X', 'Y', 'Z']
        if prediction == 'X':
            return CHOICES[self.beats[0]].value + 0
        if prediction == 'Y':
            return CHOICES[self.draws[0]].value + 3
        if prediction == 'Z':
            return CHOICES[self.loses[0]].value + 6


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


ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSORS = ['C', 'Z']

CHOICES = {
    'A': Rock(), 'X': Rock(),
    'B': Paper(), 'Y': Paper(),
    'C': Scissors(), 'Z': Scissors(),
}


def p1(f):
    data = f.read().split('\n')[:-1]
    data = map(lambda s: s.split(), data)
    score = 0
    for row in data:
        me = CHOICES[row[1]]
        score += me.versus(row[0])
        score += me.value
    return score


def p2(f):
    data = f.read().split('\n')[:-1]
    data = map(lambda s: s.split(), data)
    score = 0
    for row in data:
        opponent = CHOICES[row[0]]
        score += opponent.fulfill_prediction(row[1])
    return score
