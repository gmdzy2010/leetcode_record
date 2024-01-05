def main(s: str):
    """验证回文字符串

    Args:
        - s (str): 原字符串
    """
    ans1 = is_palindrome_2pointers(s)
    print(ans1)

    ans2 = is_palindrome_stack(s)
    print(ans2)


def is_palindrome_2pointers(s: str) -> bool:
    """验证回文字符串，双指针法

    Args:
        - s (str): 原字符串

    Returns:
        - bool: 验证结果
    """
    size = len(s)

    # * 左右两个指针
    L, R = 0, size - 1
    while L < R:
        # * 分别在左右去除非小写字母字符串
        while L < R and not s[L].isalnum():
            L += 1
        while L < R and not s[R].isalnum():
            R -= 1

        # * 判断左右指针处的小写字母是否相同
        if L < R:
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1

    return True


def is_palindrome_stack(s: str) -> bool:
    """验证回文字符串，栈法

    Args:
        - s (str): 原字符串

    Returns:
        - bool: 验证结果
    """
    stack = [c for c in s if c.isalnum()]

    for c in s:
        if c.isalnum():
            if c.lower() != stack.pop().lower():
                return False

    return True


if __name__ == "__main__":
    test_str = "afdfd"
    main(test_str)
