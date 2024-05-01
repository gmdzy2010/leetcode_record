from typing import List


def main(arr: List[int], k: int) -> int:
    """数组的第K个最大

    Args:
        arr (List[int]): 数组
        k (int): 位置

    Returns:
        int: 第K个最大的值
    """
    len_arr = len(arr)
    if len_arr < 2:
        return arr[k]

    process(arr, 0, len_arr - 1)

    return arr[k]


def process(arr: List[int], L: int, R: int):
    """处理函数

    Args:
        arr (List[int]): 原数组
        L (int): 左边界
        R (int): 右边界
    """
    if L >= R:
        return None

    P = partition(arr, L, R)
    process(arr, L, P - 1)
    process(arr, P + 1, R)

    return None


def partition(arr: List[int], L: int, R: int) -> int:
    """分区函数

    Args:
        arr (List[int]): 未排序数组
        L (int): 左边界
        R (int): 右边界

    Returns:
        int: 分区值的位置
    """
    pivot = arr[R]
    i = L - 1
    for j in range(L, R):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[R] = arr[R], arr[i + 1]

    return i + 1


if __name__ == "__main__":
    input_arr = [3, 2, 4, 4, 5, 1, 6, 0, 7, 9]
    print(main(input_arr, 3))
