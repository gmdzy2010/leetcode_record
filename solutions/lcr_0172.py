from typing import List


def main(scores: List[int], target: int) -> int:
    """已排序数组统计重复次数

    Args:
        - nums (List[int]): 已排好序的数组
        - target (int): 待查找的元素

    Returns:
        - int: 目标值的重复次数
    """
    # * 先找目标值的右边界，即目标值最后一次出现的位置
    index_1 = search(scores, target)

    # * 再找比它小的值的第一个位置
    index_2 = search(scores, target - 1)

    return index_1 - index_2


def search(nums: List[int], target: int) -> int:
    """二分搜索目标值的右边界

    虽然找的是右边界，但返回的是左边界：
    - 因为这里二分查找不是找到目标值就停止了，是还会继续向前找，直至找到最后一个目标值的位置

    Args:
        - nums (List[int]): 已排好序的数组
        - target (int): 待查找的元素

    Returns:
        - int:
            - 找到 target ，为 target 最后一次出现的位置
            - 未找到 target，为比 target 小的元素最后一个位置
    """
    # * 两个指针分别位于数组的左右边界处
    L, R = 0, len(nums) - 1
    while L <= R:
        # * 中间位置
        M = (L + R) // 2

        # * 比较 中间处的值和目标值，根据情况确定舍弃哪一半
        # ! 这里等号可以取到，说明找到了目标值 L 仍然会右移，即 L 停留在最后一个目标值的位置
        if nums[M] <= target:
            L = M + 1
        else:
            R = M - 1

    return L


if __name__ == "__main__":
    test_nums = [2, 2, 3, 4, 4, 4, 5, 6, 6, 8]
    main(test_nums, 7)
