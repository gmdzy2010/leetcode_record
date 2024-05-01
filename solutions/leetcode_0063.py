from typing import List


def main(obstacleGrid: List[List[int]]) -> int:
    """不同的路径数量，DP

    Args:
        - obstacleGrid (List[List[int]]): 包含障碍物的网格二维矩阵表示

    Returns:
        - int: 从 (0, 0) 到 (-1, -1) 的不同路径数量
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    # * 如果入口或者出口放障碍物就直接返回 0
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0

    # * dp[i][j] 代表 从 (0, 0) 到 (i, j) 共有多少条路径
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # * 从 (i, 0) 到 (i, j) 只有 1 条路径
    for i in range(m):
        # ! 注意如果初始化在任意一行遇到障碍物要提前终止初始化，以下代码是错误的
        # if obstacleGrid[i][0] == 0:
        #     dp[i][0] = 1

        if obstacleGrid[i][0] == 1:
            break

        dp[i][0] = 1

    # * 从 (0, j) 到 (i, j) 只有 1 条路径
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break

        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue

            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    test_nums = [[0, 0], [1, 1], [0, 0]]
    print(main(test_nums))
