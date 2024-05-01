def main(s: str) -> str:
    """反转字符串中的单词顺序，快慢指针法

    Args:
        - s (str): 原字符串

    Returns:
        - str: 反转单词顺序后的字符串
    """
    ans = ""
    size = len(s)
    reversed_s = s[::-1]

    S, F = 0, 0
    while F < size:
        while F < size and reversed_s[F] == " ":
            F += 1
        S = F
        while F < size and reversed_s[F] != " ":
            F += 1

        ans += reversed_s[S:F][::-1] + " "

    return ans.strip()


if __name__ == "__main__":
    test_str = "  hello world  "
    print(main(test_str))
