def main(s: str) -> str:
    """最长回文子串

    Args:
        - s (str): 原字符串

    Returns:
        - str: 最长回文子串
    """
    if not s:
        return s

    s_len = len(s)
    palindrome_len = 1
    max_palindrome_len = 0
    max_palindrome_start = 0
    for i, c in enumerate(s):
        L, R = i - 1, i + 1
        while L > 0 and s[L] == c:
            palindrome_len += 1
            L -= 1
        while R < s_len and s[R] == c:
            palindrome_len += 1
            R += 1

        while L >= 0 and R < s_len and s[L] == s[R]:
            palindrome_len += 2
            L -= 1
            R += 1

        if palindrome_len > max_palindrome_len:
            max_palindrome_len = palindrome_len
            max_palindrome_start = L

        palindrome_len = 1

    return s[
        max_palindrome_start
        + 1 : max_palindrome_start
        + 1
        + max_palindrome_len
    ]


if __name__ == "__main__":
    input_s = "babad"
    print(main(input_s))
