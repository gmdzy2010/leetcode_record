from typing import List


def main(s: str, t: str) -> bool:
    """有效的异位词

    Args:
        - s (str): 字符串1
        - t (str): 字符串2

    Returns:
        - bool: 是否为有效的异位词
    """
    # * 用数组来当哈希表
    records: List[int] = [0] * 26
    for c in s:
        records[ord(c) - ord("a")] += 1
    for c in t:
        records[ord(c) - ord("a")] -= 1

    return not any(records)


if __name__ == "__main__":
    test_s, test_t = "sadsa", "dsfasf"
    print(main(test_s, test_t))
