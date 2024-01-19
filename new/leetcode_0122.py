from typing import List


def main(prices: List[int]):
    """股票的最大利润

    Args:
        - prices (List[int]): 价格列表
    """
    ans1 = max_profit_greedy(prices)
    print(ans1)

    ans2 = max_profit_dp_2(prices)
    print(ans2)


def max_profit_greedy(prices: List[int]) -> int:
    """股票的最大利润，贪心

    Args:
        - prices (List[int]): 价格列表

    Returns:
        - int: 最大利润
    """
    max_profit = 0
    for i in range(1, len(prices)):
        # * 今天和前一天的差值
        # ! 注意买卖可以当天同时进行
        profit = prices[i] - prices[i - 1]

        # * 局部最优：收集每天的正利润
        # * 全局最优：累加的最大利润
        max_profit += max(profit, 0)

    return max_profit


def max_profit_dp_2(prices: List[int]) -> int | float:
    """买卖股票的最佳时机2，DP-二维数组

    Args:
        - prices (List[int]): 每日价格数组

    Returns:
        - int: 最大利润
    """
    size = len(prices)
    if not size:
        return 0

    # * dp[i] 当天有两个状态，持有和不持有
    # * dp[i][0]/dp[i][1] 代表第 i 天持有/不持有股票拥有的最多现金
    dp = [[0 for _ in range(2)] for _ in range(size)]

    # * 第 0 天持有股票，只能是当天买了股票
    dp[0][0] = 0 - prices[0]
    dp[0][1] = 0

    for i in range(1, size):
        # * 第 i 天持有股票有两种可能，两者取现金多的情况：
        # * 1. 第 i-1 天就持有股票 -> dp[i - 1][0]
        # * 2. 第 i-1 天不持有股票 -> dp[i - 1][1] ，第 i 天买入股票 -> - prices[i]
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])

        # * 第 i 天不持有股票也有两种可能性，两者取现金多的情况：
        # * 1. 第 i-1 天就不持有股票
        # * 2. 第 i 天卖出操作导致当天不持有股票，此时手上现金增加了 price[i]
        dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

    return dp[-1][1]


if __name__ == "__main__":
    test_nums = [7, 1, 5, 3, 6, 4]
    print(main(test_nums))
