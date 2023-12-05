from typing import List


def main(arr: List[int | float]) -> List[int | float]:
    """插入排序
    - 时间复杂度：和数据分布有关系，平均为O(N * N)，最好为O(N)
    - 空间复杂度：O(1)

    选定第 1 个元素作为左边区域，第 2~N 个元素作为右边区域，通过交换操作使得左边始终有序，则
    - 左边最右侧元素left_last一定是左侧最大

    (1)调整左侧的顺序：
    每轮循环比较左边最右侧的元素left_last和右边第一个元素right_first大小
    - left_last > right_first，交换两者，交换过来的 right_first 导致左边再次无序，
      此时 right_first 成为新的 left_last
    - 比较新的 left_last 和其左侧相邻元素的值，若 left_last 比相邻元素大，继续交换两者
    - 重复上述过程，直到左侧有序

    (2)重复(1)的操作，直到整个数组，此时整个数组有序

    Args:
        - arr (List[int | float]): 未排序数组

    Returns:
        - List[int | float]: 已排序数组
    """
    for i in range(1, len(arr)):
        j = i - 1
        right_first = arr[i]
        while j >= 0 and arr[j] > right_first:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


if __name__ == "__main__":
    input_arr: List[int | float] = [4, 1, 3, 5, 6, 8, 9, 2, 7]
    print(main(input_arr))
