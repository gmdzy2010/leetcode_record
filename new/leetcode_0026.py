from typing import List


def main(nums: List[int]) -> int:
    """有序数组移除重复元素，快慢指针法

    Args:
        - nums (List[int]): _description_

    Returns:
        - int: _description_
    """
    if not nums:
        return 0

    size = len(nums)

    # * 使用快/慢双指针 F/S，从第二个位置开始遍历
    F, S = 1, 1

    while F < size:
        # * 如果 F 处元素和 F 前一个位置元素不相等，就把  F 处元素 给 S
        if nums[F] != nums[F - 1]:
            nums[S] = nums[F]
            S += 1
        F += 1

    return S
