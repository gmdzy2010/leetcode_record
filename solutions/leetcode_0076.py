from collections import Counter


def main(s: str, t: str) -> str:
    """最小覆盖子串，滑动窗口+哈希表

    Args:
        - s (str): 原字符串
        - t (str): 待判断的被覆盖的字符串

    Returns:
        - str: s 中涵盖 t 所有字符的最小子串
    """
    size_s, size_t = len(s), len(t)

    # * 统计 t 中所有字符串的出现次数，后续次数一致即可
    cnt = Counter(t)

    # * min_len 最小覆盖子串长度
    # * diff_len 差异长度，即未覆盖（子串）长度，显然初始为字符串 t 的长度
    min_len, diff_len = size_s + 1, size_t

    L, R, ans = 0, 0, ""
    while R < size_s:
        # * 如果 s[R] 在 t 中存在，说明找到了覆盖点，未覆盖长度-1
        # ! s[R] 在 t 中不存在，cnt[s[R]] 将会因为自减操作变为负数
        if cnt[s[R]] > 0:
            diff_len -= 1

        # * 这里使用了 Counter，所以无论 s[R] 是否在 t 中存在都不会报错
        cnt[s[R]] -= 1
        R += 1

        # * 未覆盖长度为 0，说明找到了覆盖的子串，左边界右移尝试寻找更小的覆盖子串
        while diff_len == 0:
            if min_len > R - L:
                min_len = R - L
                ans = s[L:R]

            # * s[L] 在 t 中不存在，差异长度+1
            if cnt[s[L]] == 0:
                diff_len += 1

            cnt[s[L]] += 1
            L += 1

    return ans


if __name__ == "__main__":
    test_s, test_t = "ADOBECODEBANC", "ABC"
    print(main(test_s, test_t))
