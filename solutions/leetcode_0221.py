from typing import List


def main(matrix: List[List[str]]) -> int:
    """最大正方形，DP-二维

    Args:
        - matrix (List[List[int]]): "0"/"1" 构成的矩阵

    Returns:
        - int: 最大正方形的面积
    """
    ans = 0
    row, col = len(matrix), len(matrix[0])

    # * dp[i][j] 代表 [i, j] 为右下角且只包含 1 的边长最大值
    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "1":
                # * 如果此时行或列坐标为 0，"1"正方形的最大边长只能是 1
                if i == 0 or j == 0:
                    dp[i][j] = 1

                # * 当前位置的左上角最近邻三个位置都有可能得到新的最长边长
                # ! 这三个方向上取边长最小值一定能保证得到的是一个正方形，且边长最大
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1,
                    )

                # * 得到最大边长后，更新边长最大值
                ans = max(ans, dp[i][j])

    return ans * ans


if __name__ == "__main__":
    test_nums = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(main(test_nums))
