from utils import *


def p1(text: str) -> any:
    rules, updates = parse(text, lines, paragraphs)
    rules = tuple(mapt(int, r.split("|")) for r in rules)
    updates = tuple(mapt(int, u.split(",")) for u in updates)

    ans = []
    for update in updates:
        rrs = tuple((a, b) for a, b in rules if (a in update) and (b in update))

        for a, b in rrs:
            if update.index(a) - update.index(b) > 0:
                break
        else:
            middle_page_nr = update[len(update) // 2]
            ans.append(middle_page_nr)

    return sum(ans)


def p2(text: str) -> any:
    rules, updates = parse(text, lines, paragraphs)
    rules = tuple(mapt(int, r.split("|")) for r in rules)
    updates = tuple(mapt(int, u.split(",")) for u in updates)

    ans = []
    for update in updates:
        rrs = tuple((a, b) for a, b in rules if (a in update) and (b in update))

        for a, b in rrs:
            if update.index(a) - update.index(b) < 0:
                break
        else:
            do_put_in_order()
