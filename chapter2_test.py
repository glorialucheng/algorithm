from chapter2 import *

import pytest


def test_search():
    arr = [i for i in range(100)]
    key = 28
    print()
    print('index: ', seq_search(arr, key))
    print('index: ', seq_search2(arr, key))


def test_string_match():
    s = 'hello world!'
    sub = 'or'
    print()
    print('index 蛮力法: ', bf(s, sub))
    print('index by kmp: ', kmp(s, sub))


def test_sort():
    arr = [4, 2, 1, 5, 6, 0, 9]
    print()
    select_sort(arr)
    print('sorted by select_sort: ', arr)
    arr = [4, 2, 1, 5, 6, 0, 9]
    bubble_sort(arr)
    print('sorted by bubble_sort: ', arr)


def test_generate_arr():
    n = 3
    res = generate_arr(n)
    print()
    for i in range(1, n + 1):
        print('seqLength=', str(i), 'result=', res[i - 1])


def test_generate_subset():
    n = 4
    arr = ['a' + str(i) for i in range(n, 0, -1)]
    res = generate_subset(arr)
    print()
    for i in range(2 ** n):
        print('result of', str(i + 1), ': ', res[i])


def test_package_problem():
    w = [7, 3, 4, 5]
    v = [42, 12, 40, 25]
    c = 10
    print('\n', package_problem(w, v, c))


def test_task_distribute():
    c = [[9, 2, 7], [6, 4, 3], [5, 8, 1]]
    res, min_cost = task_distribute(c)
    print('\nmin cost when: ', res, ', min cost is ' + str(min_cost))
    for i in range(len(res)):
        print('Person-' + str(i) + ' do Task-' + str(res[i]))


def test_hamilton_problem():
    g = [[0, 1, 1, 1, 0],
         [1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]
    res = hamilton_problem(g)
    for i in range(len(res)):
        s = ''
        for j in res[i][:-1]:
            s += str(j) + '->'
        s += str(res[i][-1])
        print('\nHamilton回路-' + str(i + 1) + ': ', s)


def test_tsp_solution():
    g = [[0, 2, 5, 7],
         [2, 0, 8, 3],
         [5, 8, 0, 1],
         [7, 3, 1, 0]]
    res = tsp_solution(g)
    for i in range(len(res)):
        s = ''
        for j in res[i][:-1]:
            s += str(j) + '->'
        s += str(res[i][-1])
        print('\nTSP路径-' + str(i + 1) + ': ', s)


def test_closest_point():
    x = [i for i in range(10)]
    y = [i * i for i in range(10)]
    res, index1, index2 = closest_point(x, y)
    print('\nmin distend:', res, '第{}和第{}个点'.format(index1, index2))


import numpy as np


def test_convex_hull_problem():
    points = np.random.rand(30, 2)
    print('\n凸包的下标为：', convex_hull_problem(points))


if __name__ == '__main__':
    # 只运行指定的一个测试函数
    # pytest.main(['chapter2_test.py::test_search', '-s'])
    # 运行该文件中的所有测试函数
    pytest.main(['chapter2_test.py', '-s'])
