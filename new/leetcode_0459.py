from typing import List


def main(s: str) -> bool:
    """重复的子字符串

    Args:
        - s (str): 原字符串

    Returns:
        - int: 是否由某个子串重复而成
    """
    size = len(s)
    if not size:
        return False

    nexts = get_nexts(s)
    if nexts[-1] != 0 and size % (size - nexts[-1]) == 0:
        return True

    return False


def get_nexts(pattern: str) -> List[int]:
    """获取模式串的前缀表

    Args:
        - pattern (str): 模式串

    Returns:
        - List[int]: 前缀表
    """
    size = len(pattern)
    nexts = [0] * size

    # * 前缀和后缀指针分别从第一个和第二个位置开始
    prefix_i, suffix_i = 0, 1

    while suffix_i < size:
        # * 对于闭区间 prefix_i~suffix_i 上子串，
        # * 只要两个指针处的字符相同，nexts[i] 就是之前已经得到的值累加1
        if pattern[suffix_i] == pattern[prefix_i]:
            nexts[suffix_i] = prefix_i + 1
            prefix_i += 1
            suffix_i += 1

        # * 利用之前已经计算过的结果
        elif prefix_i > 0:
            prefix_i = nexts[prefix_i - 1]

        # * 其他情况 suffix_i 指针向前走一步
        else:
            suffix_i += 1

    return nexts


if __name__ == "__main__":
    test_str = "aabaabaab"
    print(main(test_str))
