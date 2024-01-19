from typing import List


def main(amount: int, coins: List[int]) -> int:
    """零钱兑换，DP-完全背包

    Args:
        - amount (int): 金额总和（背包）
        - coins (List[int]): 硬币种类（物品）

    Returns:
        - int: 凑成目标金额的组合数量
    """
    # * dp[i] 代表凑成总额为 i 的硬币组合数量
    dp = [0] * (amount + 1)

    # ? 凑成总额为 0 硬币有一种方案？？？他妈的在扯淡吧？
    dp[0] = 1

    # * 先物品再背包
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]

    return dp[-1]


if __name__ == "__main__":
    test_nums = [1, 2, 5]
    print(main(5, test_nums))
