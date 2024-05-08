from typing import List


def main(nums: List[int]) -> int:
    """最长和谐子序列，快慢指针/滑动窗口

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 和谐子序列长度
    """
    nums.sort()
    size, ans = len(nums), 0
    S, F = 0, 0
    while F < size:
        # * 相差大于1的位置，移动慢指针
        while S < F and nums[F] - nums[S] > 1:
            S += 1

        # * 剩余的则是相差等于1或者小于1的，选择小于1的位置记录长度
        if nums[F] - nums[S] == 1:
            ans = max(ans, F - S + 1)

        F += 1

    return ans


if __name__ == "__main__":
    print(main([1, 3, 2, 2, 5, 2, 3, 7]))
