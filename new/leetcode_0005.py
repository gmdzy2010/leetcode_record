def main(s: str):
    """最长回文子串

    - 中心扩散法
    - 动态规划法
    - Manacher法

    Args:
        s (str): 原字符串
    """
    ans = max_sub_palindrome_center(s)
    print(ans)

    ans = max_sub_palindrome_dp(s)
    print(ans)

    ans = max_sub_palindrome_manacher(s)
    print(ans)


def max_sub_palindrome_center(s: str) -> str:
    """最长回文子串

    中心扩散法实现
    假设当前字符串 s 遍历到了位置 i，现在以 i 为中心用左/右指针 L/R 向左右两边扩大
    - 当 i 的左边字符与 s[i] 相同，则 L 向左移动一步，回文长度 +1
    - 当 i 的右边字符与 s[i] 相同，则 R 向右移动一步，回文长度 +1
    - 当 s[L] 和 s[R] 相等，则 L/R 向 左/右移动一步，回文长度 +1
    - 更新最大回文子串长度和最大回文子串的起始位置
    - 根据长度和起始点截取最大回文子串返回

    Args:
        - s (str): 原字符串

    Returns:
        - str: 最长回文子串
    """
    if not s:
        return s

    s_len = len(s)

    # * 回文字符串长度，初始为1
    palindrome_len = 1
    max_palindrome_len = 0
    max_palindrome_start = 0
    for i, c in enumerate(s):
        # * 左右指针分别在当前位置的最左/右位置
        L, R = i - 1, i + 1

        # * 判断当前字符 c 和左右侧字符是否相等
        while L > 0 and s[L] == c:
            palindrome_len += 1
            L -= 1
        while R < s_len and s[R] == c:
            palindrome_len += 1
            R += 1

        # * 判断左指针和右指针处字符是否相等
        while L >= 0 and R < s_len and s[L] == s[R]:
            palindrome_len += 2
            L -= 1
            R += 1

        # * 更新最大回文子串长度和最大回文子串的起始位置
        if palindrome_len > max_palindrome_len:
            max_palindrome_len = palindrome_len

            # ! 注意
            # while 循环内部指针先移动再判断是否满足循环条件
            # 因此，此处左指针 L 多走了一步，要加回来
            max_palindrome_start = L + 1

        # * 重置回文子串长度至初始值
        palindrome_len = 1

    return s[max_palindrome_start : max_palindrome_start + max_palindrome_len]


def max_sub_palindrome_dp(s: str) -> str:
    """最长回文子串

    动态规划算法实现

    Args:
        - s (str): 原字符串

    Returns:
        - str: 最长回文子串
    """
    return s[:]


def max_sub_palindrome_manacher(s: str) -> str:
    """最长回文子串

    Manacher算法实现

    Args:
        - s (str): 原字符串

    Returns:
        - str: 最长回文子串
    """
    return s[:]


if __name__ == "__main__":
    input_s = "babad"
    print(main(input_s))
