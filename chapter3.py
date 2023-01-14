# 第三章，分治法


# 合并两个有序列表，结果存在arr中
def merge_array(s1, s2, arr):
    i = j = 0
    while i + j < len(arr):
        # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            arr[i + j] = s1[i]
            i += 1
        else:
            arr[i + j] = s2[j]
            j += 1


def merge_sort(arr: list):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    s1 = arr[:mid]
    s2 = arr[mid:]
    merge_sort(s1)
    merge_sort(s2)
    merge_array(s1, s2, arr)


def median3(arr: list, left: int, right: int):
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    arr[mid], arr[right - 1] = arr[right - 1], arr[mid]
    return arr[right]


def partition(arr: list, left: int, right: int):
    if left >= right:
        return
    pivot = median3(arr, left, right)
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr: list, first: int, end: int):
    if first >= end:
        return
    pivot_index = partition(arr, first, end)
    quick_sort(arr, first, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)


# 最大子序和
def max_sum(arr: list, left: int, right: int):
    if left == right:
        if arr[left] > 0:
            sum = arr[left]
        else:
            sum = 0
    else:
        mid = (left + right) // 2
        left_sum = max_sum(arr, left, mid)
        right_sum = max_sum(arr, mid + 1, right)
        s1 = 0
        lefts = 0
        for i in range(mid, left, -1):
            lefts += arr[i]
            if lefts > s1:
                s1 = lefts
        s2 = 0
        rights = 0
        for j in range(mid + 1, right):
            rights += arr[j]
            if rights > s2:
                s2 = rights
        sum = s1 + s2

        if sum < left_sum:
            sum = left_sum
        if sum < right_sum:
            sum = right_sum
    return sum


def chess_board(tr: int, tc: int, dr: int, dc: int, size: int, table, mark):
    if size == 1:
        return
    mark += 1
    count = mark
    half = size // 2
    # 小棋盘格进行递归操作
    # 左上角
    if (dr < tr + half) and (dc < tc + half):
        chess_board(tr, tc, dr, dc, half, table, mark)
    else:
        table[tr + half - 1][tc + half - 1] = count
        chess_board(tr, tc, tr + half - 1, tc + half - 1, half, table, mark)

    # 右上角
    if (dr < tr + half) and (dc >= tc + half):
        chess_board(tr, tc + half, dr, dc, half, table, mark)
    else:
        table[tr + half - 1][tc + half] = count
        chess_board(tr, tc + half, tr + half - 1, tc + half, half, table, mark)

    # 左下角
    if (dr >= tr + half) and (dc < tc + half):
        chess_board(tr + half, tc, dr, dc, half, table, mark)
    else:
        table[tr + half][tc + half - 1] = count
        chess_board(tr + half, tc, tr + half, tc + half - 1, half, table, mark)

    # 右下角
    if (dr >= tr + half) and (dc >= tc + half):
        chess_board(tr + half, tc + half, dr, dc, half, table, mark)
    else:
        table[tr + half][tc + half] = count
        chess_board(tr + half, tc + half, tr + half, tc + half, half, table, mark)


# 输入k表示有2**k个选手参加比赛
# 返回日程表
def game_table(k: int):
    res = [[0 for i in range(2 ** k)] for j in range(2 ** k)]
    n = 2 ** 1
    res[0][0] = 1
    res[0][1] = 2
    res[1][0] = 2
    res[1][1] = 1
    for _ in range(1, k):
        temp = n
        n *= 2
        # 左下角
        for i in range(temp, n):
            for j in range(temp):
                res[i][j] = res[i - temp][j] + temp  # 左下角
                res[j][i] = res[i][j]  # 右上角
                res[i][j + temp] = res[i - temp][j]  # 右下角
    return res


def closest_point(x: list, y: list):
    # todo
    pass


from scipy.spatial import ConvexHull
import numpy as np


def convex_hull_problem(points: np.ndarray):
    hull = ConvexHull(points)
    hull = hull.vertices.tolist()
    return hull
