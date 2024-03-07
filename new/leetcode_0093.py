from typing import List


def main(s: str) -> List[str]:
    """复原IP地址，回溯法

    Args:
        - s (str): 原字符串

    Returns:
        - List[str]: 所有有效的IP地址
    """
    res: List[str] = []
    ans: List[str] = []
    if len(s) > 12:
        return ans

    backtracking(s, 0, res, ans)

    return ans


def backtracking(s: str, start: int, res: List[str], ans: List[str]):
    """回溯函数

    Args:
        - s (str): 原字符串
        - start (int): 字符串开始枚举位置
        - res (List[str]): 当前处理结果列表
        - ans (List[str]): 所有合法的IP地址
    """
    p_size = len(res)
    s_size = len(s)

    # * 结果数组有了四段就判断一下是不是分完了
    if p_size == 4:
        if len("".join(res)) == s_size:
            ans.append(".".join(res))

        return

    for i in range(start, s_size):
        if not is_valid(s, start, i):
            break

        res.append(s[start : i + 1])
        backtracking(s, i + 1, res, ans)
        res.pop()


def is_valid(s: str, start: int, end: int) -> bool:
    """查看每段IP地址的合法性

    Args:
        - s (str): 原字符串
        - start (int): 开始位置
        - end (int): 结束位置

    Returns:
        - bool: 是否合法
    """
    if start > end:
        return False

    if s[start] == "0" and start != end:
        return False

    i, num = start, 0
    while i <= end:
        if not "0" <= s[i] <= "9":
            return False

        num = num * 10 + int(s[i])

        if num > 255:
            return False

        i += 1

    return True


if __name__ == "__main__":
    test_str = "25525511135"
    print(main(test_str))
