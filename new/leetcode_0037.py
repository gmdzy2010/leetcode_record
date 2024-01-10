from typing import List


def main(board: List[List[str]]) -> None:
    """解数独，回溯法

    Args:
        - board (List[List[str]]): 整个数独棋盘
    """
    backtracking(board)


def backtracking(board: List[List[str]]) -> bool:
    """回溯函数

    Args:
        - board (List[List[str]]): 整个数独棋盘

    Returns:
        - bool: 是否已经填完了
    """
    row_size, col_size = len(board), len(board[0])
    for r in range(row_size):
        for c in range(col_size):
            # * 当前位置不是点，说明不可以填数字
            if board[r][c] != ".":
                continue

            # * 看看1～9哪个数字可以填入当前位置
            for num in range(1, 10):
                # * 不合法的数字跳过
                if not is_valid(r, c, num, board):
                    continue

                # * 当前位置填入数字
                board[r][c] = str(num)

                # * 如果回溯返回True，说明已经填写完毕，可以返回
                # ! 使用回溯当递归条件有点奇怪
                if backtracking(board):
                    return True

                board[r][c] = "."

            # * 如果所有数字都不行，返回false
            return False

    # * 如果所有位置都找过了，没有返回False，说明已经填好了
    return True


def is_valid(row: int, col: int, num: int, board: List[List[str]]) -> bool:
    """判断位置的有效性

    Args:
        - row (int): 当前行
        - col (int): 当前列
        - num (int): 待填入数字
        - board (List[List[str]]): 整个数独棋盘

    Returns:
        - bool: 当前位置是否可以填入 num
    """
    # * 判断行/列是否存在重复数字
    for i in range(9):
        if board[row][i] == str(num) or board[i][col] == str(num):
            return False

    # * 判断每个9宫格内是否存在重复数字
    start_r, start_c = (row // 3) * 3, (col // 3) * 3
    for r in range(start_r, start_r + 3):
        for c in range(start_c, start_c + 3):
            if board[r][c] == str(num):
                return False

    return True


if __name__ == "__main__":
    test_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    for n in [" ".join(c) for c in test_board]:
        print(n)

    print("")

    main(test_board)

    for n in [" ".join(c) for c in test_board]:
        print(n)
