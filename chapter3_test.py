from chapter3 import *

import pytest


def test_sort():
    arr = [5, 4, 6, 3, 8, 2, 0]
    print()
    print(arr)
    merge_sort(arr)
    print(arr)
    arr = [5, 4, 6, 3, 8, 2, 0]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


def test_max_sum():
    arr = [-20, 11, -4, 13, -5, -2]
    print('\nmax sum =', max_sum(arr, 0, len(arr) - 1))


def test_chess_board():
    mark = 0
    n = 8  # 输入8*8的棋盘规格
    table = [[-1 for x in range(n)] for y in range(n)]  # -1代表特殊格子
    chess_board(0, 0, 2, 2, n, table, mark)
    n = len(table)
    print()
    for i in range(n):
        for j in range(n):
            print(table[i][j], end='\t')
        print()


def test_game_table():
    k = 3
    res = game_table(k)
    print('\n{}个玩家的日程表：'.format(2 ** k))
    for i in res:
        print(i)


def test_closest_point():
    # todo
    pass


import numpy as np


def test_convex_hull_problem():
    points = np.random.rand(30, 2)
    print('\n凸包的下标为：', convex_hull_problem(points))


if __name__ == '__main__':
    # 只运行指定的一个测试函数
    # pytest.main(['chapter3_test.py::test_merge_sort', '-s'])
    # 运行该文件中的所有测试函数
    pytest.main(['chapter3_test.py', '-s'])
