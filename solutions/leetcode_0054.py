from typing import List


def main(matrix: List[List[int]]) -> List[List[int]]:
    """螺旋矩阵

    Args:
        matrix (List[List[int]]): 原始矩阵

    Returns:
        List[List[int]]: 螺旋后的矩阵
    """
    if not matrix:
        return []

    x_size = len(matrix[0])
    y_size = len(matrix)

    # * 分别使用四个指针代表左右上下的边界
    L, R, T, B = 0, x_size - 1, 0, y_size - 1
    ans = []

    # * 分别从左到右、从上倒下、从右到左、从下到上遍历
    while True:
        # 从左到右遍历，这个过程中上边界是不变的
        for i in range(L, R + 1):
            ans.append(matrix[T][i])

        # 第一行打印完，上边界向下移动一步
        T += 1

        # 看看上边界是否到了下边界
        if T > B:
            break

        # 从上倒下遍历，这个过程中右边界保持不变
        for i in range(T, B + 1):
            ans.append(matrix[i][R])

        # 最右侧打印完，右边界向左移动一步
        R -= 1

        # 检查右边界是否到了左边界处
        if L > R:
            break

        # 从右到左遍历，下边界保持不变
        for i in range(R, L - 1, -1):
            ans.append(matrix[B][i])
        B -= 1
        if T > B:
            break

        # 从下到上遍历，左边界保持不变
        for i in range(B, T - 1, -1):
            ans.append(matrix[i][L])
        L += 1
        if L > R:
            break

    return ans


if __name__ == "__main__":
    input_matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    print(main(input_matrix))
