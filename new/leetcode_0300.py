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

    ans = 0

    # * dp[i] 代表以 nums[i] 结尾的最长递增子序列长度，全部初始化为1
    dp = [1] * size

    for i in range(size):
        # * 在 [0, i) 区间上计算出满足 nums[j] < nums[i] 条件的所有递增子序列
        for j in range(i):
            # * nums[j] < nums[i] 代表 nums[i] 可以接在 nums[j] 之后，dp[j] + 1
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

        # * 更新最长的最长的
        if dp[i] > ans:
            ans = dp[i]

    return ans


if __name__ == "__main__":
    test_nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(main(test_nums))
