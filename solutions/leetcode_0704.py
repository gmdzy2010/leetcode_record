from typing import List


def main(nums: List[int], target: int) -> int:
    """搜索排序数组

    二分法即可

    Args:
        nums (List[int]): 已排序数组
        target (int): 要搜索的数字

    Returns:
        int: 搜索到的数字位置
    """
    if not nums:
        return -1

    size = len(nums)
    L, R = 0, size - 1
    while L <= R:
        M = (L + R) // 2
        if nums[M] == target:
            return M

        if nums[M] < target:
            L = M + 1
        else:
            R = M - 1

    return -1


if __name__ == "__main__":
    input_nums = [1, 2, 3, 4, 6, 9, 11, 13, 20]
    print(main(input_nums, 11))
