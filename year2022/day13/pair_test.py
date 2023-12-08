import sys, os

sys.path.append(os.getcwd())
from year2022.day13.answer import Input


def test_pair_1():
    assert Input([1, 1, 3, 1, 1]) < Input([1, 1, 5, 1, 1])


def test_pair_2():
    assert Input([[1], [2, 3, 4]]) < Input([[1], 4])


def test_pair_3():
    assert Input([9]) > Input([[8, 7, 6]])


def test_pair_4():
    assert Input([[4, 4], 4, 4]) < Input([[4, 4], 4, 4, 4])


def test_pair_5():
    assert Input([7, 7, 7, 7]) > Input([7, 7, 7])


def test_pair_6():
    assert Input([]) < Input([3])


def test_pair_7():
    assert Input([[[]]]) > Input([[]])


def test_pair_8():
    assert Input([1, [2, [3, [4, [5, 6, 7]]]], 8, 9]) > Input(
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
    )
