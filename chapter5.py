# 第五章，动态规划


# 输入零钱面额列表，如[1, 2, 5, 10, 20, 50, 100]
# 输出最少的纸币数量
def min_num_paper_money(change_list: list, total: int):
    used = [total + 1] * (total + 1)  # 将used初始化为长度稍微大于total的数组
    used[0] = 0
    for i in range(1, len(used)):
        for j in range(len(change_list)):
            if i >= change_list[j]:
                used[i] = min(used[i - change_list[j]] + 1, used[i])

    return used[total]


# 返回斐波那契数列的前n个元素
def fibonacci_array(n: int) -> list:
    t = [0] * n
    t[1] = 1
    for j in range(2, len(t)):
        t[j] = t[j - 1] + t[j - 2]
    return t


# 输入为带权邻接矩阵g
def tsp_solution(g: list):
    # g 为距离矩阵
    n = len(g)
    cnt = 2 ** (n - 1)
    dp = [[n for col in range(cnt)] for row in range(n + 1)]
    for i in range(1, n):
        dp[i][0] = g[i][0]

    for i in range(1, cnt - 1):  # 列标(集合)
        for j in range(1, n):  # 行标
            if i & (1 << (j - 1)) == 0:  # j不在集合中
                for k in range(1, n):
                    if (1 << (k - 1)) & i:  # k在集合中
                        dp[j][i] = min(dp[j][i], g[j][k] + dp[k][i - (1 << (k - 1))])

    for k in range(1, n):
        if (1 << (k - 1)) & (cnt - 1):  # k在集合中
            dp[0][cnt - 1] = min(dp[0][cnt - 1], g[0][k] + dp[k][cnt - 1 - (1 << (k - 1))])

    return dp[0][cnt - 1]


def min_route(g: list):
    n = len(g)
    min_cost = [999] * (n + 1)
    min_cost[0] = 0
    path = [0] * n
    for i in range(1, n):
        for j in range(i):
            if g[j][i] != 0:
                cost = min_cost[j] + g[j][i]
                if cost < min_cost[i]:
                    min_cost[i] = cost
                    path[i] = j
    return min_cost, path


# 背包问题
# w: 物品重量，v: 物品价值，c: 背包容量
# 参考课件PPT
def package_problem(w: list, v: list, c: int):
    n = len(w)
    dp = [[0] * (c + 1) for i in range(n + 1)]
    x = [0] * n
    for i in range(n):
        for j in range(c):
            if j < w[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
    j = c
    for i in range(n - 1, -1, -1):
        if dp[i][j] > dp[i - 1][j]:
            x[i] = 1
            j = j - w[i]
    return dp[n - 1][c - 1]


def max_common_arr(x: list, y: list):
    m = len(x)
    n = len(y)
    z = [0] * max(m, n)
    length = [[0] * (n + 1) for i in range(m + 1)]
    status = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
                status[i][j] = 1
            elif length[i][j - 1] >= length[i - 1][j]:
                length[i][j] = length[i][j - 1]
                status[i][j] = 2
            else:
                length[i][j] = length[i - 1][j]
                status[i][j] = 3
    i = m
    j = n
    k = length[m][n]
    while i > 0 and j > 0:
        if status[i][j] == 1:
            z[k] = x[i - 1]
            k -= 1
            i -= 1
            j -= 1
        elif status[i][j] == 2:
            j -= 1
        else:
            i -= 1
    return length[m][n]


# 参考PPT
def optimal_bst(p: list):
    n = len(p)
    c = [[0] * (n + 1) for i in range(n + 1)]
    r = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        c[i][i] = p[i - 1]
        r[i][i] = i
    for d in range(1, n):
        for i in range(1, n + 1):
            j = i + d
            min_value = 9999
            mink = i
            sum = 0
            for k in range(i, j + 1):
                sum = sum + p[k - 1]
                if c[i][k - 1] + c[k + 1][j] < min_value:
                    min_value = c[i][k - 1] + c[k + 1][j]
                    mink = k
            c[i][j] = min_value + sum
            r[i][j] = mink
    return c[1][n]


# 参考PPT
def asm(p: str, t: str, k):
    m = len(p)
    n = len(t)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    res = []
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if p[i-1] == t[j-1]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        if dp[m][j] <= k:
            res.append((t[j-m:j], dp[m][j]))
    return res, dp
