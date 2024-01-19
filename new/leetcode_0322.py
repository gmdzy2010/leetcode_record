from typing import List


def main(coins: List[int], amount: int) -> int | float:
    """零钱兑换，DP-完全背包

    Args:
        - coins (List[int]): 硬币种类
        - amount (int): 目标金额

    Returns:
        int | float: _description_
    """
    # * dp[i] 代表凑成总额为 i 的最少金币数量
    dp = [float("inf")] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        # * 已经选择了 coin 剩余的金额再继续凑
        for j in range(coin, amount + 1):
            if dp[j - coin] != float("inf"):
                dp[j] = min(dp[j], dp[j - coin] + 1)

    return -1 if dp[-1] == float("inf") else dp[-1]


if __name__ == "__main__":
    test_nums = [1, 2, 5]
    print(main(test_nums, 11))
