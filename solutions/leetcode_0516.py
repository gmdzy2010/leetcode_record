def main(s: str) -> int:
    """最长回文子序列，DP-二维

    Args:
        - s (str): 原字符串

    Returns:
        - int: 最长回文子序列长度
    """
    size = len(s)

    # * dp[i][j] 代表 s 的 [i, j] 区间内的最长回文子序列长度
    dp = [[0 for _ in range(size)] for _ in range(size)]

    # * 一个字符的最长回文子序列长度是1
    for i in range(size):
        dp[i][i] = 1

    for i in range(size - 1, -1, -1):
        for j in range(i + 1, size):
            # * 如果 i/j 处的字符相等，只需要在上一个状态基础上加2即可
            # ! 上一个状态并不是 dp[i - 1][j - 1]，而是 dp[i + 1][j - 1]
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2

            # * 如果不相等，需要看看两种情况，哪个长度大
            # * 1. 不要 i 处字符，即 i 回退一步（i 倒序遍历）
            # * 2. 不要 j 处字符，即 j 回退一步
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # ! 注意这里取最右上角的值，因为状态数组是从左下角往右上角依次更新的
    return dp[0][-1]


if __name__ == "__main__":
    test_str = "bbbab"
    print(main(test_str))
