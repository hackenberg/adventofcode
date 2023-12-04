from utils import *


def parse_in1(text: str) -> tuple[set[str], set[str]]:
    parsed = re.findall(r"(\d+|\|)", text)
    separator = parsed.index("|")
    return set(parsed[1:separator]), set(parsed[separator+1:])


def p1(text: str) -> any:
    cards = parse(text, parse_in1)
    matching = [len(intersection(card)) for card in cards]
    return sum(2 ** (m - 1) for m in matching if m != 0)


def p2(text: str) -> any:
    cards = parse(text, parse_in1)
    matching = [len(intersection(card)) for card in cards]
    counts = [1] * len(cards)
    for i in range(len(cards)):
        for j in range(i+1, i+1+matching[i]):
            counts[j] += counts[i]
    return sum(counts)
