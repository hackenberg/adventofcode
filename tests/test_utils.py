from utils import *


def test_parse():
    assert parse("hello\nworld", show=0) == ('hello', 'world')
    assert parse("123\nabc7", digits, show=0) == ((1, 2, 3), (7,))


def test_parsers():
    assert atoms('hello, cruel_world! 24-7') == ('hello', 'cruel_world', 24, -7)
    assert words('hello, cruel_world! 24-7') == ('hello', 'cruel', 'world')
    assert digits('hello, cruel_world! 24-7') == (2, 4, 7)
    assert ints('hello, cruel_world! 24-7') == (24, -7)
    assert positive_ints('hello, cruel_world! 24-7') == (24, 7)


def test_truncate():
    assert truncate('hello world', 99) == 'hello world'
    assert truncate('hello world', 8) == 'hell ...'


def test_T():
    assert T([(1, 2, 3), (4, 5, 6)]) == [(1, 4), (2, 5), (3, 6)]


def test_cover():
    assert cover(3, 1, 4, 1, 5) == range(1, 6)


def test_the():
    assert the({1}) == 1


def test_intersection():
    assert intersection([{1, 2, 3}, {2, 3, 4}, {2, 4, 6, 8}]) == {2}


def test_dot_product():
    assert dot_product([1, 2, 3, 4], [1000, 100, 10, 1]) == 1234


def test_flatten():
    assert list(flatten([{1, 2, 3}, (4, 5, 6), [7, 8, 9]])) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_points_in_space():
    p, q = (0, 3), (4, 0)
    assert Y_(p) == 3 and X_(q) == 4
    assert manhattan_distance(p, q) == 7
    assert add(p, q) == (4, 3)
    assert sub(p, q) == (-4, 3)
    assert add(North, South) == (0, 0)
