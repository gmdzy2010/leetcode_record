def main(s: str) -> bool:
    """验证删除字符后回文串，双指针

    Args:
        - s (str): 原字符串

    Returns:
        - bool: 判断结果
    """
    # * 左右两个指针从左右边界开始
    L, R = 0, len(s) - 1

    while L < R:
        # * 如果左右指针处字符相等， 就相向走一步
        if s[L] == s[R]:
            L += 1
            R -= 1

        # * 左右指针处字符不相等，考虑左边或者右边删除一个字符是不是回文串
        else:
            return is_palidrome(s, L + 1, R) or is_palidrome(s, L, R - 1)

    return True


def is_palidrome(s: str, start: int, end: int) -> bool:
    """判断回文串

    Args:
        - s (str): 原字符串
        - start (int): 开始位置
        - end (int): 结束位置

    Returns:
        - bool: 判断结果
    """
    L, R = start, end
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1

    return True


if __name__ == "__main__":
    test_str = "abca"
    print(main(test_str))
