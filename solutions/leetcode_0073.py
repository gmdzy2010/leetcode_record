from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """矩阵原地置零

    Args:
        - matrix (List[List[int]]): 原矩阵
    """
    m, n = len(matrix), len(matrix[0])
    row, col = [False] * m, [False] * n

    # * 只要当前位置元素为0，就将 行/列的标志记为 True，即存在零
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True

    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j] = 0
