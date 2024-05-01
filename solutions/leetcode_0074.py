from typing import List


def main(matrix: List[List[int]], target: int):
    """搜索二维矩阵，模拟BST

    Args:
        - matrix (List[List[int]]): 二维矩阵
        - target (int): 待搜索的目标值
    """
    ans1 = search_matrix_bst(matrix, target)
    print(ans1)

    ans2 = search_matrix_bs(matrix, target)
    print(ans2)


def search_matrix_bst(matrix: List[List[int]], target: int) -> bool:
    """搜索二维矩阵，模拟BST

    Args:
        - matrix (List[List[int]]): 二维矩阵
        - target (int): 待搜索的目标值

    Returns:
        - bool: 是否可以在二维数组中找到目标值
    """
    size_row, size_col = len(matrix), len(matrix[0])

    i, j = 0, size_col - 1
    while i < size_row and j >= 0:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return True

    return False


def search_matrix_bs(matrix: List[List[int]], target: int) -> bool:
    """搜索二维矩阵，两次二分

    Args:
        - matrix (List[List[int]]): 二维矩阵
        - target (int): 待搜索的目标值

    Returns:
        - bool: 是否可以在二维数组中找到目标值
    """
    size_row, size_col = len(matrix), len(matrix[0])

    # * 将二维数组首尾相连，构成的数组也是单调递增的，可以用二分法
    L, R = 0, size_row * size_col - 1

    # ! 注意这里的边界条件
    while L <= R:
        M = (L + R) >> 1
        x, y = M // size_col, M % size_col
        if matrix[x][y] > target:
            R = M - 1
        elif matrix[x][y] < target:
            L = M + 1
        else:
            return True

    return False


if __name__ == "__main__":
    test_nums = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(main(test_nums, 16))
