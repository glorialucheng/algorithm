from chapter7 import *

import pytest


def test_color_problem():
    g = [[0, 1, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 1, 1, 0]]
    m = 3
    res = color_problem(g, m)
    print('\n着色顺序为:', res)


def test_hamilton_problem():
    g = [[0, 1, 1, 1, 0],
         [1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]
    # hamilton_problem(g)


def test_n_queue():
    n = 8
    # print('\n{}皇后问题: '.format(n), n_queue(8))


def test_batch_job():
    t1 = [2, 3, 2]
    t2 = [1, 1, 3]
    # print(batch_job(t1, t2))


if __name__ == '__main__':
    # 运行该文件中的所有测试函数
    pytest.main(['chapter7_test.py', '-s'])
