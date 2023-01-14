# 第六章，贪心法


# 输入为带权邻接矩阵g
def tsp_solution(g: list):
    n = len(g)
    flag = [0] * n  # 用于记录已走过的城市
    flag[0] = 1  # 从第0个城市出发，标志为1表示走过
    u = 0
    dest = 0
    length = 0
    while dest < n - 1:
        min_value = 9999
        for j in range(0, n):
            if flag[j] == 0 and g[u][j] != 0 and g[u][j] < min_value:
                v = j
                min_value = g[u][j]
        length += g[u][v]
        flag[v] = 1
        dest += 1
        u = v
    return length + g[u][0]


# 图着色问题
# g为无向连通图的邻接矩阵
# 返回最小颜色数
def color_problem(g: list):
    pass


# 最小生成树问题
def min_span_tree(g: list):
    pass


# 背包问题
def package_problem():
    pass


# 活动安排问题
def active_manage(s: list, f: list):
    n = len(s)
    a = [0] * n
    a[0] = 1
    j = 0
    count = 1
    for i in range(1, n):
        if s[i] >= f[j]:
            a[i] = 1
            j = i
            count += 1
    return count


def mysort(t:list, p:list):
    for i in range(len(t)):
        index = i
        for j in range(i+1, len(t)):
            if t[index] > t[j]:
                index = j
            if index != i:
                t[index], t[i] = t[i], t[index]
                p[index], p[i] = p[i], p[index]


class Task:
    def __init__(self, index, time):
        self.index = index
        self.time = time


# 多机调度问题
def arrange_machine(t: list, m: int):
    n = len(t)
    tasks = [Task(i, t[i]) for i in range(n)]
    tasks.sort(key=lambda a: a.time, reverse=True)
    d = [0]*n
    s = [[]*n]
    for i in range(m):
        s[i] = [tasks[i].index]
        d[i] = tasks[i].time
    for i in range(m, n):
        j = d.index(min(d))
        s[j].append(tasks[i].index)
        d[j] += tasks[i].time
    final_time = max(d)
    return final_time, s
