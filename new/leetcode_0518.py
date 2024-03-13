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

    # ! 当不选取任何硬币时，金额之和为 0，只有 1 种硬币组合
    dp[0] = 1

    # * 先物品再背包
    # 举个例子
    # 1. 上一轮用硬币面额 1 凑出金额 5，方案数量 dp[5]
    # 2. 这一轮用硬币面额 2 凑出金额 5，相当于凑出金额 3 的基础上加一个面额 2 的硬币就能凑
    #    成金额 5，即此种方案数量为 dp[3]
    # 3. 最终得到最新的、能够凑出金额 5 的方案总数为 dp[5] + dp[3]
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = dp[i] + dp[i - coin]

    return dp[-1]


if __name__ == "__main__":
    test_nums = [1, 2, 5]
    print(main(5, test_nums))
