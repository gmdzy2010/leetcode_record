def main(m: int, n: int) -> int:
    """不同的路径数量，DP

    Args:
        - m (int): 行数量
        - n (int): 列数量

    Returns:
        - int: 从 (0, 0) 到 (m - 1, n - 1) 的不同路径数量
    """
    # * dp[i][j] 代表 从 (0, 0) 到 (i, j) 共有多少条路径
    dp = [[0] * n] * m

    # ! 注意机器人只能向下或者向右行走
    # * 从 (i, 0) 到 (i, j) 只有 1 条路径
    for i in range(m):
        dp[i][0] = 1

    # * 从 (0, j) 到 (i, j) 只有 1 条路径
    for j in range(n):
        dp[0][j] = 1

    # ! 注意横纵向都是从第 2 行/列开始向下走，第一行已经初始化了
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(main(3, 7))
