from chapter4 import *

import pytest


def test_binary_search():
    arr = [2, 4, 5, 6, 7, 9]
    k = 5
    print()
    print(binary_search(arr, k))


def test_bst_search():
    root = BinaryNode(63)
    root.left = BinaryNode(55)
    root.left.left = BinaryNode(42)
    root.left.right = BinaryNode(58)
    root.right = BinaryNode(90)
    root.right.left = BinaryNode(70)
    k = 70
    print()
    res = bst_search(root, k)
    if res:
        print('找到该元素：', res)
    else:
        print('该元素不存在')


def test_sort():
    arr = [4, 2, 6, 3, 7, 1, 9]
    print()
    print(arr)
    insert_sort(arr)
    print(arr)


def test_select_problem():
    arr = [0, 4, 2, 6, 3, 7, 1, 9]
    n = 4
    print('\n数组中第{}小的元素：'.format(n), select_problem(arr, n))


def test_champion_game():
    r = []
    print('\n冠军是：', str(champion_game(r)))


if __name__ == '__main__':
    # 运行该文件中的所有测试函数
    pytest.main(['chapter4_test.py', '-s'])
