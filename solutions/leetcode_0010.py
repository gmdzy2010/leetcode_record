def main(s: str, p: str) -> bool:
    """正则表达式匹配，DP

    Args:
        - s (str): 字符串
        - p (str): 模式串

    Returns:
        - bool: s 和 p 是否匹配
    """
    size_s, size_p = len(s), len(p)

    # * dp[i][j] 代表 s[:i] 与 p[:j] 是否可以匹配
    dp = [[False for _ in range(size_p + 1)] for _ in range(size_s + 1)]
    dp[0][0] = True

    # * s 为空字符串，p 偶数位置为 * 号，即可匹配
    for j in range(2, size_p + 1, 2):
        dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"

    for i in range(1, size_s + 1):
        for j in range(1, size_p + 1):
            if p[j - 1] == "*":
                # * 若 s[:i] 和 p[:j-1] 可以匹配，最终可以匹配
                if dp[i][j - 2]:
                    dp[i][j] = True

                # * 若 s[:i-1] 和 p[:j] 可以匹配，且 s[i-1] == p[j-2]，最终可以匹配
                elif dp[i - 1][j] and p[j - 2] in (s[i - 1], "."):
                    dp[i][j] = True

            else:
                if dp[i - 1][j - 1] and p[j - 1] in (s[i - 1], "."):
                    dp[i][j] = True

    return dp[-1][-1]


if __name__ == "__main__":
    print(main("aaa", "ab*ac*a"))
