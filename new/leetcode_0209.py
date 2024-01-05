from typing import List


def main(nums: List[int], target: int) -> int:
    """长度最小的连续子数组，滑动窗口

    - 一般求解数组的某个连续区间的问题，都可以用滑动窗口解决
    - 滑动窗口实际上也是双指针

    Args:
        - nums (List[int]): 原数组
        - target (int): 和目标值

    Returns:
        - int: 和为目标值的连续子数组的最小长度
    """
    if not nums:
        return 0

    size = len(nums)

    # * 题意让返回最小长度，那么结果肯定不会超过 size
    ans = size + 1

    # * 记录子数组的和
    total = 0

    # * 滑动窗口的起始和结束位置
    start, end = 0, 0
    while end < size:
        # ! 注意这里累加的是滑动窗口的结束位置的值
        total += nums[end]

        # * 如果累加和等于目标值，或者比目标值大，就缩减窗口大小
        while total >= target:
            ans = min(ans, end - start + 1)

            # * 计算完本次的结果后，累加和要减掉窗口开始位置
            total -= nums[start]

            # * 窗口向前走
            start += 1

        # * 结束位置向前走
        end += 1

    return 0 if ans == size + 1 else ans


if __name__ == "__main__":
    test_nums = [2, 3, 1, 2, 4, 3]
    main(test_nums, 7)
