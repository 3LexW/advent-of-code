import sys, os

sys.path.append(os.getcwd())
from year2022.day13.answer import Pair


def test_pair_1():
    assert Pair([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]).valid_pair == True


def test_pair_2():
    assert Pair([[1], [2, 3, 4]], [[1], 4]).valid_pair == True


def test_pair_3():
    assert Pair([9], [[8, 7, 6]]).valid_pair == False


def test_pair_4():
    assert Pair([[4, 4], 4, 4], [[4, 4], 4, 4, 4]).valid_pair == True


def test_pair_5():
    assert Pair([7, 7, 7, 7], [7, 7, 7]).valid_pair == False


def test_pair_6():
    assert Pair([], [3]).valid_pair == True


def test_pair_7():
    assert Pair([[[]]], [[]]).valid_pair == False


def test_pair_8():
    assert Pair(
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], 
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
    ).valid_pair == False
