def p1(f):
    data = f.read().split('\n')
    max_calories = 0
    current_calories = 0

    for row in data:
        if not row:
            max_calories = max(max_calories, current_calories)
            current_calories = 0
            continue

        current_calories += int(row)

    return max_calories


def p2(f):
    data = f.read().split('\n')
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
