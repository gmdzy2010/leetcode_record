from typing import List


def main(s: str, k: int) -> str:
    """翻转字符串

    Args:
        - s (str): 原字符串
        - k (int): 翻转步长

    Returns:
        - str: 翻转后的字符串
    """
    list_str = list(s)
    for i in range(0, len(s), 2 * k):
        list_str[i : (i + k)] = reverse(list_str[i : (i + k)])

    return "".join(s)


def reverse(s: List[str]) -> List[str]:
    """翻转字符串

    Args:
        - s (List[str]): 字符串数组

    Returns:
        - List[str]: 翻转后的字符串数组
    """
    L, R = 0, len(s) - 1
    while L < R:
        s[L], s[R] = s[R], s[L]
        L += 1
        R -= 1

    return s
