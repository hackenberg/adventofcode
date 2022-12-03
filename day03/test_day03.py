import pytest

from day03 import find_common_item, priority

testbackpacks = [
    ('vJrwpWtwJgWrhcsFMMfFFhFp', 'p'),
    ('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'L'),
    ('PmmdzqPrVvPwwTWBwg', 'P'),
    ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'v'),
    ('ttgJtRGJQctTZtZT', 't'),
    ('CrZsJsPPZsGzwwsLwLmpwMDw', 's'),
]


@pytest.mark.parametrize('items, expected', testbackpacks)
def test_find_common_item(items, expected):
    assert expected == find_common_item(items)


testpriorities = [
    ('p', 16),
    ('L', 38),
    ('P', 42),
    ('v', 22),
    ('t', 20),
    ('s', 19),
]


@pytest.mark.parametrize('item, expected', testpriorities)
def test_priority(item, expected):
    assert expected == priority(item)
