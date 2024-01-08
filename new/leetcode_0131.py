from typing import List


def main(s: str) -> List[List[str]]:
    """分割回文串

    Args:
        - s (str): 原字符串

    Returns:
        - List[List[str]]: 所有可能的分割方案
    """
    ans: List[List[str]] = []
    res: List[str] = []
    backtracking(s, 0, res, ans)

    return ans


def is_palindrome(s: str, L: int, R: int) -> bool:
    """判断左右边界之间的字符串是否是回文

    Args:
        - s (str): 原字符串
        - L (int): 左边界
        - R (int): 右边界

    Returns:
        - bool: 是否是回文
    """
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1

    return True


def backtracking(
    s: str,
    start: int,
    res: List[str],
    ans: List[List[str]],
):
    """回溯递归函数

    Args:
        - s (str): 原字符串
        - start (int): 回溯开始位置
        - res (List[str]): 可能的分割方案
        - ans (List[List[str]]): 所有可能的分割方案
    """
    size = len(s)
    if start >= size:
        ans.append(res[:])
        return

    for i in range(start, size):
        if is_palindrome(s, start, i):
            res.append(s[start : i + 1])
        else:
            continue

        backtracking(s, i + 1, res, ans)

        res.pop()


if __name__ == "__main__":
    test_str = "abbac"
    main(test_str)
