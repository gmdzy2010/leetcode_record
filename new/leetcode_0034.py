from typing import List


def main(nums: List[int], target: int) -> List[int]:
    """有序数组查找元素首末位置，二分法

    Args:
        - nums (List[int]): 有序数组，有重复
        - target (int): 待查找值

    Returns:
        - List[int]:
            - 首次出现的位置和最后一次出现的位置
            - 如果未找到，返回[-1, -1]
    """
    if not nums:
        return [-1, -1]

    size = len(nums)
    first_i = -1
    last_i = -1

    # * 第一次二分查找，找第一次出现目标值的位置
    L, R = 0, size - 1
    while L <= R:
        M = (L + R) // 2
        # ! 注意这里找到的 target 位置还不是最终的 first_i
        if nums[M] == target:
            # * 有可能的目标位置，后续继续收敛地去找第一个目标位置
            first_i = M

            # ! 因为要找第一次目标值出现的位置，需要向左找，所以这里下次的右边界往左边缩小
            R = M - 1
        elif nums[M] > target:
            R = M - 1
        else:
            L = M + 1

    # * 第二次二分查找，找最后一次出现目标值的位置
    L, R = 0, size - 1
    while L <= R:
        M = (L + R) // 2
        if nums[M] == target:
            last_i = M

            # ! 因为要找最后一次目标值出现的位置，需要向右找，所以这里下次的左边界往右扩大
            L = M + 1
        elif nums[M] > target:
            R = M - 1
        else:
            L = M + 1

    return [first_i, last_i]


if __name__ == "__main__":
    test_nums = [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 10]
    main(test_nums, 7)
