# 第二章，蛮力法


# 顺序查找
import math


def seq_search(array: list, key: int):
    index = len(array) - 1
    while index >= 0 and array[index] != key:
        index -= 1
    return index


# 改进的顺序查找
def seq_search2(array: list, key: int):
    array.append(key)
    index = 0
    while array[index] != key:
        index += 1
    return index


# 串匹配问题，蛮力法
def bf(s: str, subs: str):
    i = j = 0
    while i < len(s) and j < len(subs):
        if s[i] == subs[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == len(subs):
        return i - j
    else:
        return -1


def kmp(s: str, subs: str):
    nextArr = get_next_array(subs)
    i = j = 0
    while i < len(s) and j < len(subs):
        if s[i] == subs[j]:
            i += 1
            j += 1
        elif j > 0:
            j = nextArr[j - 1]
        else:
            i += 1
    if j == len(subs):
        return i - j
    else:
        return -1


def get_next_array(s: str):
    nextArr = [0]
    j = 1
    k = 0  # k表示当前公共前后缀长度
    while j < len(s):
        if s[j] == s[k]:
            j += 1
            k += 1
            nextArr.append(k)
        else:
            if k == 0:
                nextArr.append(0)
                j += 1
            else:
                k = nextArr[k - 1]
    return nextArr


def select_sort(arr: list):
    for i in range(len(arr) - 1):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        if index != i:
            arr[i], arr[index] = arr[index], arr[i]


def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 生成排列对象
# 开始      1
# 插入2     12   21
# 插入3     123  132  312  213  231  321
# ...

from itertools import permutations


def generate_arr(n: int):
    arr = [i for i in range(1, n + 1)]
    res = []
    for i in range(1, n + 1):
        # 调用系统函数库，生成长度不同的排列对象
        res.append(list(permutations(arr, i)))
    # 返回所有排列，即长度为1、2、3...n的排列
    return res


# 生成子集
def generate_subset(arr: list):
    n = len(arr)
    res = []
    for i in range(2 ** n):
        temp = []
        s = bin(i)[2:].zfill(n)
        for j in range(len(s)):
            if s[j] == '1':
                temp.append(arr[j])
        res.append(temp)
    return res


# 背包问题
# w: 物品重量，v: 物品价值，c: 背包容量
def package_problem(w: list, v: list, c: int):
    if len(w) != len(v):
        exit(1)
    all_w = generate_subset(w)
    all_v = generate_subset(v)
    weights = []
    values = []
    for i in range(len(all_w)):
        temp_w = 0
        temp_v = 0
        for j in all_w[i]:
            temp_w += j
        for k in all_v[i]:
            temp_v += k
        weights.append(temp_w)
        values.append(temp_v)
    # for i in range(len(all_w)):
    #     print('组合：', all_w[i], 'weight: ', weights[i], 'value: ', values[i])
    max_value = 0
    index = -1
    for i in range(len(all_w)):
        if values[i] > max_value and weights[i] <= c:
            max_value = values[i]
            index = i
    # 返回最大价值的物品组合，包括每个物品的重量、价值，和总价值
    return all_w[index], all_v[index], max_value


# 任务分配问题
# c为代价矩阵，如下矩阵表示任务1给人员1代价为1，任务2给人员1代价为2
#   任务1 任务2
# [[1,    2]  人员1
#  [3,    4]] 人员2
#
# 返回分配方式、最小代价
# 如分配方式为(2, 1, 3)表示
# Person-0 do Task-2
# Person-1 do Task-1
# Person-2 do Task-3
def task_distribute(c: list):
    index = generate_arr(len(c))[len(c) - 1]
    cost = []
    for i in index:
        temp = 0
        for j in range(len(i)):
            temp += c[j][i[j] - 1]
        cost.append(temp)
    min_cost = float('inf')
    for i in range(len(cost)):
        if cost[i] < min_cost:
            min_cost = cost[i]
    return index[cost.index(min_cost)], min_cost


# 使用蛮力法解决该问题的基本思想：
# 对于给定的无向图G=(V, E)，首先生成图中所有顶点的排列对象(vi1, vi2, …, vin)，
# 然后依次考察每个排列对象是否满足以下两个条件：
# （1）相邻顶点之间存在边，即 (vij, vij+1)∈E（1≤j≤n-1）
# （2）最后一个顶点和第一个顶点之间存在边，即 (vin, vi1)∈E
# 满足这两个条件的回路就是哈密顿回路。
# 函数输入为无向图g的邻接矩阵
# 输出为路径，即哈密顿回路
def hamilton_problem(g: list):
    n = len(g)
    index = generate_arr(n)[n - 1]  # index为路径的集合
    res = []  # 所有符合条件的路径
    for i in index:  # 第i条路径
        for j in range(len(i) - 1):
            if g[i[j] - 1][i[j + 1] - 1] == 0:
                break
            if j == len(i) - 2 and g[i[n - 1] - 1][i[0] - 1] != 0:
                res.append(i)
    return res


# 输入为带权邻接矩阵g
def tsp_solution(g: list):
    all_hamilton = hamilton_problem(g)  # 获取所有的哈密顿回路，再分别计算cost
    cost = []
    for i in all_hamilton:
        temp = 0
        for j in range(len(i) - 1):
            temp += g[i[j] - 1][i[j + 1] - 1]
        temp += g[i[len(i) - 1] - 1][i[0] - 1]
        cost.append(temp)
    min_cost = min(cost)
    res = []  # 符合条件的最短路径
    for i in range(len(cost)):
        if cost[i] == min_cost:
            res.append(all_hamilton[i])
    return res


# 最近对问题，在几个点集合中，寻找距离最近的距离
def closest_point(x: list, y: list):
    n = len(x)
    index1 = -1
    index2 = -1
    min_distend = 10000
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            if d < min_distend:
                min_distend = d
                index1 = i
                index2 = j
    return math.sqrt(min_distend), index1, index2


from scipy.spatial import ConvexHull
import numpy as np


def convex_hull_problem(points: np.ndarray):
    hull = ConvexHull(points)
    hull = hull.vertices.tolist()
    return hull
