from typing import List


def main(nums: List[int], target: int) -> int:
    """组合总和4，DP-完全背包

    根据数据规模（约 10**2），回溯会超时

    Args:
        - nums (List[int]): 原数组
        - target (int): 目标和

    Returns:
        - int: 排列组合个数
    """
    # * dp[i] 代表总和为 i 的排列组合个数
    dp = [0] * (target + 1)

    dp[0] = 1

    for i in range(target + 1):
        for num in nums:
            # * 因为先枚举目标和（背包），物品（数字）有可能超过背包容量
            if i - num >= 0:
                dp[i] += dp[i - num]

    return dp[-1]


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(main(test_nums, 5))
