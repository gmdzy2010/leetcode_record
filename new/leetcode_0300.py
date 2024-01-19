from typing import List


def main(nums: List[int]) -> int:
    """最长递增子序列，DP

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 最长递增子序列长度
    """
    if not nums:
        return 0

    size = len(nums)

    # * dp[i] 代表以 nums[i] 结尾的最长递增子序列长度，全部初始化为1
    dp = [1] * size

    for i in range(size):
        # * 在 [0, i) 区间上计算出满足 nums[j] < nums[i] 条件的所有递增子序列
        for j in range(i):
            # * nums[j] < nums[i] 代表 nums[i] 可以接在 nums[j] 之后，dp[j] + 1
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # * 最后还需计算 dp的最大值
    # ? 为什么呢？
    # * 每次计算的都只是以 nums[i] 结尾的最长递增子序列长度，要比较一次所有的长度
    return max(dp)


if __name__ == "__main__":
    test_nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(main(test_nums))
