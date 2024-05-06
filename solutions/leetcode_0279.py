from math import sqrt


def main(n: int) -> int | float:
    """完全平方数，DP-完全背包

    Args:
        - n (int): 目标数字

    Returns:
        - int | float: 得到 n 需要的最少平方数
    """
    # * dp[i] 代表凑成 i->背包 的最少 平方数->物品 数量
    dp = [float("inf")] * (n + 1)

    dp[0] = 0

    # * 物品：平方小于 n 的所有数字，可以任意选择
    for i in range(1, int(sqrt(n)) + 1):
        x = i * i
        for j in range(x, n + 1):
            # * 取两者之间更小的：
            # * 不使用当前平方数
            # * 使用当前平方数 i*i，然后在此基础上加 1（因为用了 i*i），即 f[j-i*i] + 1
            dp[j] = min(dp[j], dp[j - x] + 1)

    return dp[-1]


if __name__ == "__main__":
    print(main(9))
