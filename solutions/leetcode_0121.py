from typing import List


def main(prices: List[int]):
    """买卖股票的最佳时机1
    - 贪心
    - 动态规划

    Args:
        - prices (List[int]): 每日价格数组
    """
    ans1 = max_profit_greedy(prices)
    print(ans1)

    ans2 = max_profit_dp(prices)
    print(ans2)


def max_profit_greedy(prices: List[int]) -> int | float:
    """买卖股票的最佳时机1，贪心

    Args:
        - prices (List[int]): 每日价格数组

    Returns:
        - int: 最大利润
    """
    # * 核心思想是找到左侧最低价格，在差价最高的时候卖出
    # ! 贪心的核心在于，只要数据没完就不断找局部的最小/最大，知道完成枚举
    min_price = float("inf")
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)

    return max_profit


def max_profit_dp(prices: List[int]) -> int | float:
    """买卖股票的最佳时机1，DP

    - dp[i] 表示前 i 天的最大利润
    - 则当前的最大利润是截止至前一天的最大利润 dp[i - 1] 和 今天的利润之间的最大值
        - max(dp[i - 1], dp[i] - price[i])

    Args:
        - prices (List[int]): 每日价格数组

    Returns:
        - int: 最大利润
    """
    size = len(prices)
    if not size:
        return 0

    min_price = prices[0]

    # * dp[i] 表示第 i 天卖出所获得的利润
    # ? 这里为什么不是 size + 1，不能最后一天卖出？
    dp = [0] * size
    for i in range(1, size):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - min_price)

    return dp[-1]


def max_profit_dp_2(prices: List[int]) -> int | float:
    """买卖股票的最佳时机1，DP-二维数组

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
        # * 1. 第 i-1 天就持有股票
        # * 2. 第 i 天买入操作导致当天有了股票，显然买入之前持有的现金为 0
        dp[i][0] = max(dp[i - 1][0], 0 - prices[i])

        # * 第 i 天不持有股票也有两种可能性，两者取现金多的情况：
        # * 1. 第 i-1 天就不持有股票
        # * 2. 第 i 天卖出操作导致当天不持有股票，此时手上现金增加了 price[i]
        dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

    return dp[-1][1]


if __name__ == "__main__":
    input_nums = [7, 1, 5, 3, 6, 4]
    print(main(input_nums))
