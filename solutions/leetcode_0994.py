from collections import deque
from typing import Deque, List, Tuple


def main(grid: List[List[int]]) -> int:
    """腐烂的橘子，BFS

    Args:
        - grid (List[List[int]]): 橘子坐标

    Returns:
        - int: 橘子都腐烂的最短时间
    """
    row, col, ans = len(grid), len(grid[0]), 0
    rottens: Deque[Tuple[int, int, int]] = deque()
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 2:
                rottens.appendleft((r, c, ans))

    while rottens:
        r, c, ans = rottens.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            _r, _c = r + dr, c + dc
            if _r in range(row) and _c in range(col) and grid[_r][_c] == 1:
                grid[_r][_c] = 2
                rottens.appendleft((_r, _c, ans + 1))

    # ! 如果感染完仍然有新鲜的橘子，那么返回 -1
    for row in grid:
        if 1 in row:
            return -1

    return ans


if __name__ == "__main__":
    test_grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    print(main(test_grid))
