def main(s: str, t: str) -> int:
    """不同的子序列，DP-二维

    等价于问题：s 删除几个字符串后等于 t，有几种方案

    Args:
        - s (str): 原字符串
        - t (str): 模式串，其长度小于等于 s

    Returns:
        - int: s 子序列等于 t 的个数
    """
    size_1, size_2 = len(s), len(t)

    # * dp[i][j] 代表以 s[i-1] 结尾的子序列中，以 t[j-1] 结尾的子序列出现次数
    dp = [[0 for _ in range(size_2 + 1)] for _ in range(size_1 + 1)]

    # * 若 s 和 t 均为空字符串时结果是 1
    dp[0][0] = 1

    # * dp[i][0] 代表 s 在 (0,i-1) 区间任意选择得到空字符串(j为 0)的子序列个数
    for i in range(1, size_1 + 1):
        dp[i][0] = 1

    # * dp[0][j] 代表 s 为空字符串时构成 t 的子序列个数，显然无论如何不可能构成 t
    for j in range(1, size_2 + 1):
        dp[0][j] = 0

    for i in range(1, size_1 + 1):
        # ! 这里可以剪枝，模式串比字符串大的部分不需要考虑
        for j in range(1, size_2 + 1):
            # ! 当 s[i - 1] 等于 t[j - 1]时，字符 s[i - 1] 选/不选择都需要考虑
            # ? 为什么呢？
            # * 比如 s = "bagg"，t = "bag", s[3] 选/不选是两种子序列，但都可以匹配上
            # * 用字符 s[i - 1] -> dp[i - 1][j]
            # * 不用字符 s[i - 1] -> dp[i - 1][j - 1]
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

            # * 当 s[i - 1] 不等于 t[j - 1] 时，肯定不选 s[i - 1]，因为选了也不匹配
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


if __name__ == "__main__":
    test_str1, test_str2 = "baegg", "bag"
    print(main(test_str1, test_str2))
