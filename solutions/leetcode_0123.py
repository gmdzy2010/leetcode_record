from typing import List


def main(prices: List[int]) -> int:
    """买卖股票的最佳时机2，DP-二维数组

    Args:
        - prices (List[int]): 每日价格数组

    Returns:
        - int: 最大利润
    """
    size = len(prices)
    if not size:
        return 0

    # * dp[i][j] 代表第 i 天状态 j 下的最多的现金
    dp = [[0 for _ in range(5)] for _ in range(size)]

    # ! 每天共有 5 种状态
    # 0 -> 观望
    dp[0][0] = 0

    # 1 -> 第一次持有
    # dp[0][1] = 0 - prices[0]
    dp[0][1] = -prices[0]

    # 2 -> 第一次不持有
    # dp[0][2] = 0 - prices[0] + prices[0]
    dp[0][2] = 0

    # 3 -> 第二次持有
    # dp[0][3] = 0 - prices[0] + prices[0] - prices[0]
    dp[0][3] = -prices[0]

    # 4 -> 第二次不持有
    # dp[0][4] = 0 - prices[0] + prices[0] - prices[0] + prices[0]
    dp[0][4] = 0

    for i in range(1, size):
        # * 第 i 天观望
        dp[i][0] = dp[i - 1][0]

        # * 第 i 天第一次持有股票有两种可能性，两者取现金多的情况：
        # * 1. 第 i-1 天就持有股票 -> dp[i - 1][1]
        # * 2. 第 i 天买入操作导致：第一次持有 -> dp[i - 1][0] - prices[i]
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        # * 第 i 天第一次不持有股票有两种可能性，两者取现金多的情况：
        # * 1. 第 i 天没有操作，沿用第 i-1 天状态：第一次不持有 -> dp[i - 1][2]
        # * 2. 第 i 天卖出操作导致：第一次不持有 -> dp[i - 1][1] + prices[i]
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])

        # * 第 i 天第二次持有股票有两种可能性，两者取现金多的情况：
        # * 1. 第 i 天没有操作，沿用第 i-1 天状态：第二次持有 -> dp[i - 1][3]
        # * 2. 第 i 天卖出操作导致：第二次持有 -> dp[i - 1][2] - prices[i]
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])

        # * 第 i 天第二次不持有股票有两种可能性，两者取现金多的情况：
        # * 1. 第 i 天没有操作，沿用第 i-1 天状态：第二次不持有 -> dp[i - 1][4]
        # * 2. 第 i 天卖出操作导致当天第二次不持有 -> dp[i - 1][3] + prices[i]
        dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

    return dp[-1][4]


if __name__ == "__main__":
    test_nums = [3, 3, 5, 0, 0, 3, 1, 4]
    print(main(test_nums))
