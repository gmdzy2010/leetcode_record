from typing import List


def main(strs: List[str]) -> str:
    """最长公共前缀，纵向扫描法

    Args:
        - strs (List[str]): 字符串列表

    Returns:
        - str: 最长公共前缀
    """
    if not strs:
        return ""

    size = len(strs)

    # * 取列表的首个字符串 strs[0] 作为起始扫描字符串
    # * 再取后续的字符串 strs[j] 挨个进行比较
    for i, c in enumerate(strs[0]):
        for j in range(1, size):
            # * 有两种情况说明已经达到了最长公共前缀
            # * 1. strs[j] 长度和 strs[0] 已经遍历过的字符串长度相等
            # * 2. strs[j] 和 strs[0] 的第 i 个字符相同
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]

    return strs[0]


if __name__ == "__main__":
    test_strs = ["lee", "leetcode", "left"]
    main(test_strs)
