from typing import List


def main(digits: str) -> List[str]:
    """电话号码组合

    Args:
        - digits (str): 数字字符串

    Returns:
        - List[str]: 所有组合结果
    """
    if not digits:
        return []

    res, ans = [], []
    letters_map = [
        "",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz",
    ]
    backtracking(letters_map, digits, 0, res, ans)

    return ans


def backtracking(
    letters_map: List[str],
    digits: str,
    index: int,
    res: List[str],
    ans: List[str],
):
    """回溯函数

    Args:
        - letters_map (List[str]): 数字和英文字母的映射数组
        - digits (str): 数字字符串
        - index (int): 开始位置
        - res (List[str]): 可能的组合
        - ans (List[str]): 组合结果列表
    """
    size = len(digits)
    # * 到达边界就结束回溯并记录结果
    if index == size:
        ans.append("".join(res))
        return

    letters = letters_map[int(digits[index])]
    for c in letters:
        res.append(c)
        backtracking(letters_map, digits, index + 1, res, ans)
        res.pop()


if __name__ == "__main__":
    test_str = "23"
    print(main(test_str))
