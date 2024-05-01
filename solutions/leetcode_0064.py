from typing import List


def main(grid: List[List[int]]):
    """最小路径和，DP-二维

    Args:
        - grid (List[List[int]]): 二维数组
    """
    ans1 = min_sum_path_dp(grid)
    print(ans1)

    ans2 = min_sum_path_dp_2D(grid)
    print(ans2)


def min_sum_path_dp(grid: List[List[int]]) -> int:
    """最小路径和，DP-无数组

    Args:
        - grid (List[List[int]]): 二维数组

    Returns:
        - int: 最小路径
    """
    row, col = len(grid), len(grid[0])

    for i in range(row):
        for j in range(col):
            # * 起点
            if i == 0 and j == 0:
                grid[i][j] = grid[0][0]

            # * 只能往右走
            elif i == 0:
                grid[i][j] = grid[i][j - 1] + grid[i][j]

            # * 只能向下走
            elif j == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j]

            # * 不在边界处
            else:
                grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

    return grid[-1][-1]


def min_sum_path_dp_2D(grid: List[List[int]]) -> int:
    """最小路径和，DP-二维

    Args:
        - grid (List[List[int]]): 二维数组

    Returns:
        - int: 最小路径
    """
    row, col = len(grid), len(grid[0])

    # * dp[i][j] 代表从左上方到当前位置的和最小的路径
    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            # * 起点
            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]

            # * 只能往右走，dp[i][j] 只能由相邻左侧的状态转移而来
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]

            # * 只能向下走，dp[i][j] 只能由相邻上方的状态转移而来
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]

            # * 不在边界的话，dp[i][j] 由最相邻的左/上方中的较小方向转移而来
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

    return dp[-1][-1]


if __name__ == "__main__":
    test_nums = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(main(test_nums))
