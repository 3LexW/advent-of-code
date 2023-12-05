import sys, os

sys.path.append(os.getcwd())
from year2023.day5.answer import split_range

cut_from, cut_to = 20, 30


def test_split_range_only_left():
    range_from, range_to = 0, 15
    left, cut, right = split_range(range_from, range_to, cut_from, cut_to)
    assert left == [0, 15]
    assert cut == None
    assert right == None


def test_split_range_only_right():
    range_from, range_to = 35, 50
    left, cut, right = split_range(range_from, range_to, cut_from, cut_to)
    assert left == None
    assert cut == None
    assert right == [35, 50]


def test_split_range_only_mid():
    range_from, range_to = 21, 30
    left, cut, right = split_range(range_from, range_to, cut_from, cut_to)
    assert left == None
    assert cut == [21, 30]
    assert right == None


def test_split_range_range1():
    range_from, range_to = 15, 25
    left, cut, right = split_range(range_from, range_to, cut_from, cut_to)
    assert left == [15, 19]
    assert cut == [20, 25]
    assert right == None


def test_split_range_range2():
    range_from, range_to = 25, 35
    left, cut, right = split_range(range_from, range_to, cut_from, cut_to)
    assert left == None
    assert cut == [25, 30]
    assert right == [31, 35]


def test_split_range_range3():
    range_from, range_to = 5, 35
    left, cut, right = split_range(range_from, range_to, cut_from, cut_to)
    assert left == [5, 19]
    assert cut == [20, 30]
    assert right == [31, 35]
