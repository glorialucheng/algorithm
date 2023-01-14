from chapter6 import *

import pytest


def test_tsp_solution():
    g = [[0, 3, 6, 7],
         [5, 0, 2, 3],
         [6, 4, 0, 2],
         [3, 7, 5, 0]]
    res = tsp_solution(g)
    print('\n最短路径：', res)


def test_active_manage():
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [i for i in range(4, 15)]
    print('\n活动安排问题', active_manage(s, f))


def test_arrange_machine():
    t = [2, 14, 4, 16, 6, 5, 3]
    m = 3
    # res, s = arrange_machine(t, m)
    # print()
    # print(res)
    # print(s)


if __name__ == '__main__':
    # 运行该文件中的所有测试函数
    pytest.main(['chapter6_test.py', '-s'])
