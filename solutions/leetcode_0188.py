from typing import List


def main(k: int, prices: List[int]) -> int:
    """买卖股票的最佳时机4，DP-二维

    Args:
        - k (int): 交易次数上限
        - prices (List[int]): 每日价格数组

    Returns:
        - int: 最大利润
    """
    size = len(prices)
    if size == 0:
        return 0

    # * dp[i] 代表第 i 天在 2k+1 个状态下最多的现金
    # ! 除了第 0 天，每笔交易都会导致状态数量增加 2，总的状态数量即 2k+1
    dp = [[0 for _ in range(2 * k + 1)] for _ in range(size)]

    for j in range(1, 2 * k, 2):
        dp[0][j] = -prices[0]

    for i in range(1, size):
        for j in range(0, 2 * k - 1, 2):
            # * 第 i 天第 j 次持有股票而现金最多的两种可能性：
            # * 1. 第 i 天观望，沿用第 i-1 天第 j 次持有
            # * 1. 第 i 天买入，导致第 i 天第 j 次持有
            dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])

            # * 第 i 天第 j 次不持有股票而现金最多的两种可能性：
            # * 1. 第 i 天观望，沿用第 i-1 天第 j 次不持有
            # * 1. 第 i 天卖出，导致第 i 天第 j 次不持有
            dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])

    return dp[-1][2 * k]


if __name__ == "__main__":
    test_nums = []
    print(main(4, test_nums))
