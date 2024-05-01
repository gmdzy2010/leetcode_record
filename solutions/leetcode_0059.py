from typing import List


def main(n: int) -> List[List[int]]:
    """旋转矩阵逆过程

    Args:
        - n (int): 行列的维度

    Returns:
        - List[List[int]]: 结果
    """
    L, R, T, B = 0, n - 1, 0, n - 1
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    start, end = 1, n * n
    while start <= end:
        for l in range(L, R + 1):
            matrix[T][l] = start
            start += 1
        T += 1

        # * 从上到下，右边界 R 保持不变
        # ! matrix[t][R] 而非 matrix[R][t]
        for t in range(T, B + 1):
            matrix[t][R] = start
            start += 1
        R -= 1

        for r in range(R, L - 1, -1):
            matrix[B][r] = start
            start += 1
        B -= 1

        for b in range(B, T - 1, -1):
            matrix[b][L] = start
            start += 1
        L += 1

    return matrix


if __name__ == "__main__":
    print(main(5))
