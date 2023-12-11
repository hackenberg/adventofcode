from utils import *


def hand_strength(hand):
    match [c for _, c in Counter(hand).most_common()]:
        case 5, *_: return 1
        case 4, *_: return 2
        case 3, 2, *_: return 3
        case 3, *_: return 4
        case 2, 2, *_: return 5
        case 2, *_: return 6
        case _: return 7


def parse_in1(line: str) -> tuple[str, int]:
    hands, bid = line.split()
    return hands, int(bid)


def p1(text: str) -> any:
    card_labels = "AKQJT98765432"
    records = list(parse(text, parse_in1))
    records.sort(
        key=lambda r: (hand_strength(r[0]), [card_labels.index(card) for card in r[0]]),
        reverse=True
    )
    return sum((i + 1) * r[-1] for i, r in enumerate(records))


def p2(text: str) -> any:
    card_labels = "AKQT98765432J"
    in1 = parse(text, parse_in1)

    records = []
    for hand, bid in in1:
        s = hand_strength(hand)
        for sub in cross_product(card_labels[:-1], repeat=hand.count("J")):
            s = min(s, hand_strength(hand.replace("J", "") + "".join(sub)))
        records.append((s, [card_labels.index(card) for card in hand], bid))

    records.sort(reverse=True)
    return sum((i + 1) * r[-1] for i, r in enumerate(records))
