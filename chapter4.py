# 第四章，减治法


def binary_search(arr: list, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1


class BinaryNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bst_search(root: BinaryNode, k):
    if not root:
        return None
    elif root.data == k:
        return root
    elif root.data > k:
        return bst_search(root.left, k)
    else:
        return bst_search(root.right, k)


def insert_sort(arr: list):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp


def heap_sort(arr: list):
    # todo
    pass


# 选择arr中第k小的元素作为返回值
def select_problem(arr: list, n):
    arr.sort()
    return arr[n - 1]


class Player:
    def __init__(self):
        pass


# champion_game调用
def compete(p1: Player, p2: Player) -> bool:
    pass


# 淘汰赛冠军问题
def champion_game(r: list):
    n = len(r)
    if not n:
        return None
    while n > 1:
        n = n // 2
        for i in range(n):
            if compete(r[i + n], r[i]):
                r[i] = r[i + n]
    return r[0]
