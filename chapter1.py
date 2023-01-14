# 第一章， 绪论


# 求两个自然数m和n的最大公约数
# ⑴ 至少设计出三个版本的求最大公约数算法，用伪代码描述各个算法；
# ⑵ 对所设计的算法采用大O符号进行时间复杂性分析；
# 欧几里得算法
# 定理：两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数
# 时间复杂度O(log n)
def get_max_common_factor1(a: int, b: int):
    mod = a % b
    while mod != 0:
        a = b
        b = mod
        mod = a % b
    return b


# 暴力循环求解
# 时间复杂度O(n)
def get_max_common_factor2(a: int, b: int):
    s = a if a < b else b
    while s > 0:
        if a % s == 0 and b % s == 0:
            return s
        s -= 1


# 更相减损术
# 1、先判断两个数的大小，如果两数相等，则这个数本身就是就是它们的最大公约数。
# 2、如果不相等，则用大数减去小数，然后用这个较小数与它们相减的结果相比较，如果相等，则这个差就是它们的最大公约数，而如果不相等，则继续执行操作2。
# 时间复杂度O(n)
def get_max_common_factor3(a: int, b: int):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# 前N个自然数的随机序列
# 编写程序，产生前N个自然数的随机序列，如N为5时，{4,3,1,5,2} 和{3,1,4,2,5} 都是正确的，但 {5,4,1,2,1} 就是错误的，因为少了数字3，数字1重复了。
# 至少采用两种算法，分析其时间复杂度
# N取值分别为1千,1万,10万,100万,1000万
# 用表格的形式给出不同N的T和O表达式的值，以及真实运行时间，并画出散点图或折线图

from random import randint


# 暴力求解，逐个生成数字
# 如果生成的数字不在里面则填入，否则重新生成
# 只用到了一个数组
def get_random_sequence1(n: int):
    arr = [0 for _ in range(n)]
    for i in range(n):
        while True:
            temp = randint(1, n)
            if temp not in arr:
                arr[i] = temp
                break
    return arr


# 另外设置一个“标志”数组，用于记录数字是否已存在
def get_random_sequence2(n: int):
    arr = [0 for _ in range(n)]
    flag = [0 for _ in range(n)]
    for i in range(n):
        temp = randint(1, n)
        while flag[temp - 1] == 1:
            temp = randint(1, n)
        arr[i] = temp
        flag[temp - 1] = 1
    return arr


# 先生成1到n得顺序序列
# 将第i个数字与前面随机一个数字对调
# O(n)
def get_random_sequence3(n: int):
    arr = [i + 1 for i in range(n)]
    for index in range(n):
        temp = randint(0, index)
        arr[index], arr[temp] = arr[temp], arr[index]
    return arr
