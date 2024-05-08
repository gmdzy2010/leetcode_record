from typing import List


def main(s: str, words: List[str]) -> bool:
    """检查字符串是否为数组前缀

    Args:
        - s (str): 字符串
        - words (List[str]): 单词列表

    Returns:
        - bool: s是否由 words 的前 k 项拼接而成
    """
    ans, n = "", len(s)
    for w in words:
        ans += w
        if ans == s:
            return True
        elif len(ans) > n:
            return False

    return False
