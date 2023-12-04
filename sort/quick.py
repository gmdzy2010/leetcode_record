from typing import List


def main(arr: List[int | float]) -> List[int | float]:
    """快速排序，时间复杂度O(N * logN)
    选定最右侧元素作为划分阈值pivot，分别针对 >pivot 和 <=pivot的数字分区

    Args:
        arr (List[int | float]): 未排序数组

    Returns:
        List[int|float]: 已排序数组
    """
    if len(arr) <= 1:
        return arr

    return arr


if __name__ == "__main__":
    input_arr = [2, 1, 3, 5, 4, 7, 9, 8, 6]
    print(main(input_arr))
