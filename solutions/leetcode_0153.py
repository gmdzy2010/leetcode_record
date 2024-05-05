from typing import List


def main(nums: List[int]) -> int:
    """在旋转排序数组中搜索最小值，二分法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 最小值
    """
    L, R = 0, len(nums) - 1
    while L <= R:
        M = (L + R) // 2
        # * 如果中点值比右边界小，那么最小一定在 M 左侧，舍弃右边即可
        if nums[M] < nums[R]:
            # ! 这里不能取 R = M - 1，这样可能会把恰好处于 M 处的最小值遗漏掉
            R = M
        elif nums[M] > nums[R]:
            L = M + 1
        else:
            return nums[M]

    return -1
