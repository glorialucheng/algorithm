from chapter5 import *

import pytest


def test_min_num_paper_money():
    change = [1, 2, 5, 10, 20, 50, 100]
    total = 17
    print('\n纸币面额有：', change)
    print('共{}元，至少需要{}张纸币'.format(total, min_num_paper_money(change, total)))


def test_fibonacci_array():
    n = 10
    print('\n斐波那契的前{}个元素为：'.format(n), fibonacci_array(n))


def test_tsp_solution():
    g = [[999, 3, 6, 7],
         [5, 999, 2, 3],
         [6, 4, 999, 2],
         [3, 7, 5, 999]]
    res = tsp_solution(g)
    print('\n最短路径：', res)


def test_min_route():
    g = [[0, 4, 2, 3, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 6, 7, 8, 0, 0, 0],
         [0, 0, 0, 0, 0, 4, 7, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 5, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 6, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    min_cost, path = min_route(g)
    for i in range(len(g)):
        print('\n到顶点{}的最小开销为{}'.format(i, min_cost[i]), '路径：', i, end='')
        pre = i
        while path[pre]:
            print(' <-', path[pre], end='')
            pre = path[pre]


def test_package_problem():
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 9]
    c = 10
    print('\n', package_problem(w, v, c))


def test_max_common_arr():
    x = ['a', 'b', 'c', 'b', 'd', 'b']
    y = ['a', 'c', 'b', 'b', 'a', 'b', 'd', 'b', 'b']
    print('\n最长公共子序列长度为：', max_common_arr(x, y))


def test_optimal_bst():
    p = [0.1, 0.2, 0.4, 0.3]
    # print(optimal_bst(p))


def test_asm():
    p = 'happy'
    t = 'have a hsppy day'
    k = 1
    res, dp = asm(p, t, k)
    print()
    print(res)
    for i in dp:
        for j in i:
            print(j, '\t', end='')
        print()


if __name__ == '__main__':
    # 运行该文件中的所有测试函数
    pytest.main(['chapter5_test.py', '-s'])
