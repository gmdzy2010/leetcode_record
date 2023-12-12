from typing import List


def main(grid: List[List[str]]) -> int:
    """岛屿问题

    使用递归感染的方式
    - 时间复杂度：O(N * M)

    Args:
        - grid (List[List[str]]): 岛屿矩阵数组

    Returns:
        - int: 岛屿个数
    """
    ans = 0
    if not grid or not grid[0]:
        return ans

    x_size = len(grid)
    y_size = len(grid[0])
    for i in range(x_size):
        for j in range(y_size):
            if grid[i][j] == "1":
                ans += 1
                infect(grid, i, j, x_size, y_size)
    return ans


def infect(grid: List[List[str]], i: int, j: int, x_size: int, y_size: int):
    """感染函数

    - 保证位置不能跑到界外
    - grid[i][j] != 1 -> 停止感染，返回
    - 将当前位置设置为 2，即为感染
    - grid[i][j] == 1 -> 在当前位置的上/下/左/右四个方向上递归感染

    Args:
        matrix (List[List[str]]): 原始矩阵
        i (int): x坐标
        j (int): y坐标
        x_size (int): x方向维度
        y_size (int): y方向维度
    """
    if i not in range(x_size) or j not in range(y_size) or grid[i][j] != "1":
        return

    grid[i][j] = "2"
    infect(grid, i, j + 1, x_size, y_size)
    infect(grid, i + 1, j, x_size, y_size)
    infect(grid, i, j - 1, x_size, y_size)
    infect(grid, i - 1, j, x_size, y_size)


if __name__ == "__main__":
    matrix = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"],
        ["1", "0", "0", "0", "1"],
    ]
    print(main(matrix))
