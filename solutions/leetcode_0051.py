from typing import List


def main(n: int) -> List[List[str]]:
    """N皇后问题

    Args:
        - n (int): 皇后数量

    Returns:
        - List[List[str]]: n个皇后的放置方案
    """
    # * 棋盘位置用二维的点阵模拟
    res = [["." for _ in range(n)] for _ in range(n)]
    ans: List[List[str]] = []

    backtracking(n, 0, res, ans)

    return ans


def backtracking(n: int, row: int, res: List[List[str]], ans: List[List[str]]):
    """回溯函数

    Args:
        - n (int): 皇后数量
        - row (int): 当前处理的行
        - res (List[List[str]]): 棋盘
        - ans (List[List[str]]): 所有放置方案
    """
    # * 放置完成，记录当前放置方案并结束递归
    if row == n:
        ans.append(["".join(c) for c in res])
        return

    for col in range(n):
        if is_valid(n, row, col, res):
            res[row][col] = "Q"

            # * 每行设置一个Q位置，然后就去下一行
            backtracking(n, row + 1, res, ans)

            res[row][col] = "."


def is_valid(n: int, row: int, col: int, res: List[List[str]]) -> bool:
    """判断当前位置是否可以放置皇后

    Args:
        - n (int): 皇后数量
        - row (int): 行数
        - col (int): 列数
        - res (List[List[str]]): 棋盘

    Returns:
        - bool: 是否合法
    """
    # * 检查列
    # ? 为什么是剪枝操作？
    for r in range(row):
        if res[r][col] == "Q":
            return False

    # * 检查左上方45度斜线位置是否合法
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if res[r][c] == "Q":
            return False

    # * 检查右上方135度斜线位置是否合法
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if res[r][c] == "Q":
            return False

    return True


if __name__ == "__main__":
    print(main(5))
