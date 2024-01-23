def main(s: str):
    """最长回文子串长度，DP-二维

    Args:
        - s (str): 原字符串
    """
    ans1 = get_max_palindrome_dp(s)
    print(ans1)

    ans2 = get_max_palindrome_2pointers(s)
    print(ans2)


def get_max_palindrome_dp(s: str) -> int:
    """最长回文子串长度，DP-二维

    Args:
        - s (str): 原字符串

    Returns:
        - int: 最长回文子串长度
    """
    size = len(s)
    ans = 0

    # * dp[i][j] 代表 [i, j] 区间内的字符是否是回文串
    dp = [[False for _ in range(size)] for _ in range(size)]

    # ! 倒着遍历保证回文区间搜索的判断准确性
    for i in range(size - 1, -1, -1):
        for j in range(i, size):
            # * 当 i 和 j 位置处的字符相等时：
            # 1. 下标相同或者相邻，区间内是回文串
            # 2. i 与 j 相向压缩区间一步，看看此时的区间是否是回文区间
            if s[i] == s[j]:
                if j - i <= 1:
                    ans += 1
                    dp[i][j] = True

                elif dp[i + 1][j - 1]:
                    ans += 1
                    dp[i][j] = True

    return ans


def get_max_palindrome_2pointers(s: str) -> int:
    """最长回文子串长度，双指针

    Args:
        - s (str): 原字符串

    Returns:
        - int: 最长回文子串长度
    """
    size = len(s)
    ans = 0
    for i in range(size):
        # ! 分别计算一个中心点和两个中心点的情况
        ans += extend(s, i, i)
        ans += extend(s, i, i + 1)

    return ans


def extend(s: str, L: int, R: int) -> int:
    """获取区间内回文串个数

    Args:
        - s (str): 原字符串
        - L (int): 左边界
        - R (int): 右边界

    Returns:
        - int: 区间内回文串的个数
    """
    res = 0
    size = len(s)
    # * 当左右边界处的字符相等就向外扩展边界
    while L >= 0 and R < size and s[L] == s[R]:
        L -= 1
        R += 1
        res += 1

    return res


if __name__ == "__main__":
    test_str = "aabac"
    print(main(test_str))
