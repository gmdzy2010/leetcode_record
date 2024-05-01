def main(word1: str, word2: str) -> int:
    """字符串删除操作，DP-二维

    Args:
        - word1 (str): 字符串1
        - word2 (str): 字符串2

    Returns:
        - int: 最少的操作
    """
    size_1, size_2 = len(word1), len(word2)

    # * dp[i][j] 代表让以 word1[i-1]/word2[j-1] 结尾的两个字符串最少操作次数
    dp = [[0 for _ in range(size_2 + 1)] for _ in range(size_1 + 1)]

    # * dp[i][0] 代表 word2 是空字符串，word1 变成 word2 最少需要几次操作
    for i in range(1, size_1 + 1):
        dp[i][0] = i

    # * dp[0][j] 同理
    for j in range(1, size_2 + 1):
        dp[0][j] = j

    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            # * word1[i - 1] 等于 word2[j - 1]，此时不需要操作
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # * word1[i - 1] 不等于 word2[j - 1]，此时有 2 种选择：
            # * 1. 删除其中一个字符
            # * 2. 两个字符都删除
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 2,
                )

    return dp[-1][-1]


if __name__ == "__main__":
    test_str1, test_str2 = "sea", "sae"
    print(main(test_str1, test_str2))
