from typing import List


def main(matrix: List[List[int]], target: int) -> bool:
    """搜索二维矩阵

    Args:
        - matrix (List[List[int]]): 二维矩阵
        - target (int): 待搜索的目标值

    Returns:
        - bool: 是否存在 target
    """
    row, col = len(matrix), len(matrix[0])
    r, c = 0, col - 1
    while c >= 0 and r < row:
        if target < matrix[r][c]:
            c -= 1
        elif target > matrix[r][c]:
            r += 1
        else:
            return True

    return False


if __name__ == "__main__":
    test_nums = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(main(test_nums, 20))
