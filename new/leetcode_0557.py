def main(s: str) -> str:
    """反转字符串中的单词，快慢指针法

    Args:
        - s (str): 原字符串

    Returns:
        - str: 反转单词后的字符串
    """
    ans = ""
    size = len(s)
    S, F = 0, 0
    while F < size:
        # * 先走过所有空格
        while F < size and s[F] == " ":
            F += 1
            ans += " "

        # * 慢指针从非空格处开始计数
        S = F

        # * 快指针走过接下来所有非空格字符串
        while F < size and s[F] != " ":
            F += 1

        # * 把这一段直接反转拼接到结果中去
        ans += s[S:F][::-1]

    return ans


if __name__ == "__main__":
    test_str = "Let's take LeetCode contest"
    print(main(test_str))
