from typing import List


def main(nums: List[int]) -> int:
    """缺失的第一个正数，哈希数组法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 缺失的第一个正数
    """
    size = len(nums)
    for i in range(size):
        # * 如果当前位置元素和当前位置元素-1 所对应的数字不相等
        # * 就交换他们
        while nums[i] in range(1, size) and nums[i] != nums[nums[i] - 1]:
            # ! 这个错误：nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
            # ? 为什么？
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(size):
        if i + 1 != nums[i]:
            return i + 1

    return size + 1


if __name__ == "__main__":
    test_nums = [7, 8, 9, 11, 12]
    print(main(test_nums))
