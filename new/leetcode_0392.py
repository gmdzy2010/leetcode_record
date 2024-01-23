def main(s: str, t: str):
    """判断子序列

    Args:
        - s (str): 待判断子序列
        - t (str): 原字符串

    Returns:
        - bool: s 是否是 t 的子序列
    """
    ans1 = is_sub_sequence_2pointers(s, t)
    print(ans1)

    ans2 = is_sub_sequence_dp(s, t)
    print(ans2)


def is_sub_sequence_2pointers(s: str, t: str) -> bool:
    """判断子序列，双指针

    Args:
        - s (str): 待判断子序列
        - t (str): 原字符串

    Returns:
        - bool: s 是否是 t 的子序列
    """
    if not s:
        return True

    i = 0
    for c in t:
        if s[i] == c:
            i += 1
            if i == len(s):
                return True

    return False


def is_sub_sequence_dp(s: str, t: str) -> bool:
    """判断子序列，DP-二维

    Args:
        - s (str): 待判断子序列
        - t (str): 原字符串

    Returns:
        - bool: s 是否是 t 的子序列
    """
    size_1, size_2 = len(s), len(t)

    # * dp[i][j] 代表以 s/t 的第 i/j 个字符结尾的子串相同字符个数
    dp = [[0 for _ in range(size_2 + 1)] for _ in range(size_1 + 1)]

    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[-1][-1] == size_1


if __name__ == "__main__":
    test_str1, test_str2 = "abc", "acbdec"
    print(main(test_str1, test_str2))
