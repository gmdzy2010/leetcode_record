def main(text1: str, text2: str) -> int:
    """最长公共子序列，DP

    Args:
        - text1 (str): 字符串1
        - text2 (str): 字符串2

    Returns:
        - int: 最长公共子序列长度
    """

    size_1, size_2 = len(text1), len(text2)

    # * dp[i][j] 代表在 text1/text2 的 (0, i-1)/(0, j-1) 区间上的最长公共子序列长度
    # ! dp[i][0] 和 dp[0][j] 都没有意义
    dp = [[0 for _ in range(size_2 + 1)] for _ in range(size_1 + 1)]

    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            # * 如果两个字符串当前字符相等，就在 dp[i - 1][j - 1] 基础上累加1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # * 不相等需要回退其中一个字符串的字符看看哪个公共子序列更长
            # * 1. (0, i-2)/(0, j-1) 区间上的最长公共子序列长度
            # * 2. (0, i-1)/(0, j-2) 区间上的最长公共子序列长度
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == "__main__":
    test_str1, test_str2 = "abcde", "ace"
    print(main(test_str1, test_str2))
