#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.read().split('\n')

max_calories = 0
current_calories = 0

for row in data:
    if not row:
        max_calories = max(max_calories, current_calories)
        current_calories = 0
        continue

    current_calories += int(row)

print(max_calories)
