def main(n: int) -> int:
    """爬楼梯

    Args:
        - n (int): 数字

    Returns:
        - int: 总共的方案
    """
    if n < 2:
        return n

    # * dp[i] 代表跳跃 n 个台阶的方案数量
    # ! 因为 0 没有意义，所以 dp 数组多一个元素
    dp = [0] * (n + 1)

    # * 初始化没有dp[0]，其没有意义
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]


if __name__ == "__main__":
    print(main(7))
