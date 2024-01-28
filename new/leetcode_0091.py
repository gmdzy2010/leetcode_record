def main(s: str) -> int:
    """数字字符串解码方案，DP-一维

    Args:
        - s (str): 数字字符串

    Returns:
        - int: 有效的解码方案数量
    """
    size = len(s)

    # * 加一个前导空格可以降低负数等判断
    s = " " + s

    # * dp[i] 代表前 i 个字符串的解码方案
    dp = [0] * (size + 1)

    dp[0] = 1

    for i in range(1, size + 1):
        a = ord(s[i]) - ord("0")
        b = (ord(s[i - 1]) - ord("0")) * 10 + a

        # * 当前数字既能单独解码，也可以和前一位数组合并在一起解码
        # ! 满足以上条件可以认为是爬楼梯问题、斐波那契数列问题
        if a in range(1, 10) and b in range(10, 27):
            dp[i] = dp[i - 1] + dp[i - 2]

        # * 当前数字只能单独解码
        elif a in range(1, 10) and b not in range(10, 27):
            dp[i] = dp[i - 1]

        # * 当前位只能和前一位合并解码，实际上就是 "10"、"20"这两种情况
        elif a not in range(1, 10) and b in range(10, 27):
            dp[i] = dp[i - 2]

        # * 对于连续的0
        else:
            dp[i] = 0

    return dp[-1]


if __name__ == "__main__":
    test_str = "0"
    print(main(test_str))
