from collections import Counter


def minWindow(s: str, t: str) -> str:
    size_s, size_t = len(s), len(t)
    cnt = Counter(t)
    L, R, min_len, ans = 0, 0, size_s + 1, ""

    valid_len = size_t

    while R < size_s:
        if cnt[s[R]] > 0:
            valid_len -= 1

        cnt[s[R]] -= 1

        R += 1

        while valid_len == 0:
            if min_len > R - L:
                min_len = R - L
                ans = s[L:R]
            if cnt[s[L]] == 0:
                valid_len += 1

            cnt[s[L]] += 1
            L += 1

    return ans
