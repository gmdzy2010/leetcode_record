from typing import List


def main(board: List[List[str]], word: str) -> bool:
    """搜索单词，回溯法

    Args:
        - board (List[List[str]]): 字符二维数组
        - word (str): 待搜索的单词

    Returns:
        - bool: 单词是否在二维数组中找到
    """
    row, col = len(board), len(board[0])
    for r in range(row):
        for c in range(col):
            if backtracking(0, r, c, word, board):
                return True

    return False


def backtracking(
    i: int,
    r: int,
    c: int,
    word: str,
    board: List[List[str]],
) -> bool:
    """回溯函数

    Args:
        - i (int): 当前字符在单词中的位置
        - r (int): 行数
        - c (int): 列数
        - word (str): 待搜索的单词
        - board (List[List[str]]): 字符二维数组

    Returns:
        bool: 二维字符数组当前位置的上下左右有没有字符和单词相等
    """
    row, col = len(board), len(board[0])
    if r not in range(row) or c not in range(col) or board[r][c] != word[i]:
        return False

    # * 当到达 word 最后一个字符，说明找到了目标单词，停止回溯
    if i == len(word) - 1:
        return True

    # * 将当前位置置空，实际上是标记为位置已访问
    board[r][c] = ""
    L = backtracking(i + 1, r, c - 1, word, board)
    R = backtracking(i + 1, r, c + 1, word, board)
    U = backtracking(i + 1, r - 1, c, word, board)
    D = backtracking(i + 1, r + 1, c, word, board)
    board[r][c] = word[i]

    # ? 这里为啥要返回四个方向的或结果
    # * 有3层含义
    # * 1. 任意一个方向匹配上，返回 True，意味着还可以继续匹配
    # * 2. 如果到了这一步四个方向都返回 False，说明没找到这个单词，可以结束搜索了
    return L or R or U or D


if __name__ == "__main__":
    test_board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    test_word = "ABCCED"
    main(test_board, test_word)
