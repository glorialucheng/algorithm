# 图着色问题
# g为代价矩阵
# m为颜色种类数


def ok(g: list, k: int, color: list) -> bool:
    for i in range(1, k):
        if g[k][i] == 1 and color[i] == color[k]:
            return False
    return True


def color_problem(g: list, m: int):
    n = len(g)
    color = [0] * n
    k = 0
    while k >= 0 and k < n:
        color[k] = color[k] + 1
        while color[k] <= m:
            if ok(g, k, color):
                break
            else:
                color[k] = color[k] + 1
        if color[k] <= m and k == n:
            break
        elif color[k] <= m and k < n:
            k += 1
        else:
            color[k] = 0
            k -= 1
    return color


# 哈密顿回路
def hamilton_problem(g: list):
    n = len(g)
    x = [i for i in range(n)]
    visited = [0] * n
    k = 1
    visited[0] = 1
    x[0] = 1
    while k > 0:
        x[k] = x[k] + 1
        while x[k] <= n:
            if visited[x[k]] == 0 and g[x[k - 1]][x[k]] == 1:
                break
            else:
                x[k] = x[k] + 1
        if x[k] <= n and k == n and g[x[k]][0] == 1:
            return
        elif x[k] <= n and k < n:
            visited[x[k]] = 1
            k += 1
        else:
            x[k] = 0
            visited[x[k]] = 0
            k -= 1
    return x


# 八皇后问题

def place_ok(k: int) -> bool:
    pass


def n_queue(n: int):
    x = [0] * n
    k = 0
    while k >= 0:
        x[k] = x[k] + 1
        while x[k] <= n and place_ok(k):
            x[k] = x[k] + 1
        if x[k] <= n and k == n:
            return
        elif x[k] <= n and k < n:
            k += 1
        else:
            x[k] = 0
            k -= 1
    return x


# 批处理作业调度问题
def batch_job(t1: list, t2: list):
    n = len(t1)
    x = [0] * (n + 1)
    sum1 = [0] * (n + 1)
    sum2 = [0] * (n + 1)
    k = 1
    best_time = 9999
    while k >= 1:
        x[k] = x[k] + 1
        while x[k] <= n:
            if ok(k):
                sum1[k] = sum1[k - 1] + t1[x[k]]
                sum2[k] = max(sum1[k], sum2[k - 1]) + t2[x[k]]
                if sum2[k] < best_time:
                    break
                else:
                    x[k] = x[k] + 1
        if x[k] <= n and k < n:
            k += 1
        else:
            if x[k] <= n and k == n:
                if best_time > sum2[k]:
                    best_time = sum2[k]
                return
        x[k] = 0
        k -= 1
    return x
