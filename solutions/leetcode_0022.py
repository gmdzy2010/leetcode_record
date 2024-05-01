from typing import List


def main(n: int) -> List[str]:
    """括号生成

    Args:
        - n (int): 总括号对数

    Returns:
        - List[str]: 所有有效的括号组合方式
    """
    res: List[str] = []
    ans: List[str] = []
    backtracking(n, n, res, ans)

    return ans


def backtracking(L: int, R: int, res: List[str], ans: List[str]):
    """回溯函数

    Args:
        - L (int): 剩余左括号数量
        - R (int): 剩余右括号数量
        - res (List[str]): 可能的组合方案
        - ans (List[str]): 所有可能的组合方案
    """
    if L == 0 and R == 0:
        ans.append("".join(res))
        return

    # * 每次回溯保证左括号用一个，右括号就用一个
    if L > R:
        return

    if L > 0:
        res.append("(")
        backtracking(L - 1, R, res, ans)
        res.pop()

    if R > 0:
        res.append(")")
        backtracking(L, R - 1, res, ans)
        res.pop()


if __name__ == "__main__":
    test_nums = 5
    print(main(test_nums))
