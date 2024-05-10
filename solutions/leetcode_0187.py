from typing import List


def main(s: str) -> List[str]:
    """重复的DNA序列，哈希表

    Args:
        - s (str): DNA序列字符串

    Returns:
        - List[str]: 满足条件的DNA序列子串
    """
    ans, size, cnt, limit = [], len(s), {}, 10

    # ? 这里为什么要+1?
    # * 这里limit是长度限制，而size是位置，之间相差1
    for i in range(size - limit + 1):
        window = s[i : i + limit]
        if window in cnt:
            cnt[window] += 1
        else:
            cnt[window] = 1

    for s, c in cnt.items():
        if c > 1:
            ans.append(s)

    return ans


if __name__ == "__main__":
    test_case = "AAAAAAAAAAA"
    print(main(test_case))
