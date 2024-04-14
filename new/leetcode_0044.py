def main(s: str, p: str) -> bool:
    """字符串匹配

    Args:
        - s (str): 字符串
        - p (str): 模式串

    Returns:
        - bool: 字符串是否可以用模式串匹配
    """
    size_s, size_p = len(s), len(p)

    # * dp[i][j] 代表 模式 p[:i-1] 是否可以匹配 字符串 s[:j-1]
    dp = [[False for _ in range(size_s + 1)] for _ in range(size_p + 1)]
    dp[0][0] = True

    # * 模式串为 "*" 号代表可以匹配包括空字符在内的任意字符串 ，
    for i in range(1, size_p + 1):
        if p[i - 1] == "*":
            dp[i][0] = True
        else:
            break

    for i in range(1, size_p + 1):
        for j in range(1, size_s + 1):
            if p[i - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

            elif p[i - 1] == "?" and s[j - 1].isalnum():
                dp[i][j] = dp[i - 1][j - 1]

            elif p[i - 1].lower() == s[j - 1].lower():
                dp[i][j] = dp[i - 1][j - 1]

    return dp[-1][-1]


if __name__ == "__main__":
    test_s, test_p = "test1.txt", "te*.txt"
    main(test_s, test_p)
