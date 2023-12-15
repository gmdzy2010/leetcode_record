from typing import List


def main(prices: List[int]):
    max_profit = max_profit_normal(prices)
    print(max_profit)


def max_profit_normal(prices: List[int]) -> int | float:
    """买卖股票的最佳时机

    Args:
        - prices (List[int]): 每日价格数组

    Returns:
        - int: 最大利润
    """
    min_price = float("inf")
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)

    return max_profit


def max_profit_dp(prices: List[int]) -> int | float:
    """买卖股票的最佳时机

    动态规划求解
    - dp[i] 表示前 i 天的最大利润，
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
    dp: List[int | float] = [0] * size
    for i in range(1, size):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - min_price)

    return dp[-1]


if __name__ == "__main__":
    input_nums = [7, 1, 5, 3, 6, 4]
    print(main(input_nums))
