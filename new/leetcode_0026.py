from typing import List


def main(nums: List[int]) -> int:
    """有序数组移除重复元素，快慢指针法

    Args:
        - nums (List[int]): 存在重复元素的有序数组

    Returns:
        - int: 删除重复元素后的新长度
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

            # * 有多少不重复元素 S 就走了多少步，
            # ! S 停留在最后一个不重复元素的下一个位置
            S += 1

        # * F 处出现了重复元素就一直往前走
        F += 1

    return S


if __name__ == "__main__":
    test_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    main(test_nums)
