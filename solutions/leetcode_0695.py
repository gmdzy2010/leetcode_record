from typing import List


def main(grid: List[List[int]]) -> int:
    """岛屿的最大面积

    Args:
        - grid (List[List[int]]): 岛屿矩阵

    Returns:
        - int: 最大面积
    """
    ans = 0
    row, col = len(grid), len(grid[0])
    for r in range(row):
        for c in range(col):
            ans = max(get_area(grid, r, c), ans)

    return ans


def get_area(grid: List[List[int]], r: int, c: int) -> int:
    """获取岛屿面积

    Args:
        - grid (List[List[int]]): 数据矩阵
        - r (int): 当前行
        - c (int): 当前列

    Returns:
        int: _description_
    """
    row, col = len(grid), len(grid[0])
    if r not in range(row) or c not in range(col) or grid[r][c] != 1:
        return 0

    # * 找到 1 的方块，面积累加1，并将此位置归零，防止下次递归重复计算
    grid[r][c] = 0
    area = 1

    for step_r, step_c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        area += get_area(grid, r + step_r, c + step_c)

    return area


if __name__ == "__main__":
    test_grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    print(main(test_grid))
