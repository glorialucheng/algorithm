# 请大家安装和使用pytest 测试框架，步骤如下：
# 1. 安装 pytest
# 命令行安装的命令  pip install pytest
# 2. 把自己的算法代码和测试代码分别放到两个文件中，
# 命名方式示例：算法代码文件 alg.py， 测试代码文件为alg_test.py
# 测试的函数必须是test_ 开头，比如 test_permutation( )
# 3. pytest使用示例：
# 在测试代码文件alg_test.py中，添加如下代码：
# if __name__ == '__main__':
#     # 只运行指定的一个测试函数
#     pytest.main(['alg_test.py::test_permutation','-s'])
#     # 运行该文件中的所有测试函数
#     #pytest.main(['alg_test.py','-s'])
# 4. 运行alg_test.py 文件
import time

import pytest
from chapter1 import *


def test_get_max_common_factor():
    loops = 10000
    a = randint(1, 100000)
    b = randint(1, 100000)
    t = time.time()
    for i in range(loops):
        get_max_common_factor1(a, b)
    print('\nget_max_common_factor1 run time: ', time.time() - t)

    t = time.time()
    for i in range(loops):
        get_max_common_factor2(a, b)
    print('\nget_max_common_factor2 run time: ', time.time() - t)

    t = time.time()
    for i in range(loops):
        get_max_common_factor3(a, b)
    print('\nget_max_common_factor3 run time: ', time.time() - t)


import matplotlib.pyplot as plt


def test_get_random_sequence():
    nums = [i * 100 for i in range(1, 51)]
    t1 = []
    t2 = []
    t3 = []
    for n in nums:
        temp = time.time()
        get_random_sequence1(n)
        t1.append(time.time() - temp)

        temp = time.time()
        get_random_sequence2(n)
        t2.append(time.time() - temp)

        temp = time.time()
        get_random_sequence3(n)
        t3.append(time.time() - temp)

    plt.plot(t1)
    plt.plot(t2)
    plt.plot(t3)
    plt.xlabel('Sequence length * 100')
    plt.ylabel('Time / s')


    plt.savefig('chapter1')
    plt.show()


if __name__ == '__main__':
    # 只运行指定的一个测试函数
    # pytest.main(['chapter1_test.py::test_get_max_common_factor', '-s'])
    pytest.main(['chapter1_test.py::test_get_random_sequence', '-s'])
    # 运行该文件中的所有测试函数
    # pytest.main(['chapter1_test.py', '-s'])
