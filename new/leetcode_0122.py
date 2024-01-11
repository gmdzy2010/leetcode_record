from typing import List


def main(prices: List[int]) -> int:
    """股票的最大利润

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


if __name__ == "__main__":
    test_nums = [7, 1, 5, 3, 6, 4]
    print(main(test_nums))
