def main(n: int) -> int:
    """拆分数字使乘积最大，DP

    Args:
        - n (int): 待拆分数字

    Returns:
        - int: 最大乘积
    """
    # * dp[i] 代表分拆数字 i 可以得到的最大乘积
    dp = [0] * (n + 1)

    # * 无法拆分 0 和 1
    dp[2] = 1
    for i in range(3, n + 1):
        # * 相当于拆分 j
        for j in range(1, i):
            # * j * (i - j) 代表把整数拆分成两个数字相乘
            # * j * dp[i - j] 代表把 i - j 再拆分
            # ? 没懂
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

    return dp[n]


if __name__ == "__main__":
    print(main(7))
