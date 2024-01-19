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


if __name__ == "__main__":
    input_nums = [7, 1, 5, 3, 6, 4]
    print(main(input_nums))
