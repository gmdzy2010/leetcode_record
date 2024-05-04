from copy import deepcopy
from typing import List


def main(matrix: List[List[int]]) -> None:
    """旋转图像

    Args:
        - matrix (List[List[int]]): 图像矩阵
    """
    size = len(matrix)
    tmp = deepcopy(matrix)
    for i in range(size):
        for j in range(size):
            _i, _j = j, size - 1 - i
            matrix[_i][_j] = tmp[i][j]


if __name__ == "__main__":
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    main(test_matrix)
