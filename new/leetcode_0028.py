from typing import List


def main(s: str, p: str) -> int:
    """字符串第一个匹配位置

    Args:
        - s (str): 原字符串
        - p (str): 模式串

    Returns:
        - int: 匹配到的开始位置
    """
    if not p:
        return 0

    s_size, p_size = len(s), len(p)
    nexts = get_nexts(p)

    s_i, p_i = 0, 0
    while s_i < s_size:
        # * 两个指针处的字符相同的情况
        if s[s_i] == p[p_i]:
            # * 已经完成匹配了，返回一开始匹配上的位置
            if p_i == p_size - 1:
                return s_i - p_i

            # * 没有到 p 尾部，两个指针都往前走，看看后面的字符是否相同
            s_i += 1
            p_i += 1

        # * 两个指针处字符不相等但 p 指针不为0
        # ! 说明有一部分匹配上了，p 指针不必归 0，利用前缀表加速
        elif p_i > 0:
            p_i = nexts[p_i - 1]

        # * 两个指针处字符不相等，s 指针往前走一步，重新开始匹配
        else:
            s_i += 1

    return -1


def get_nexts(pattern: str) -> List[int]:
    """获取模式串的前缀表

    Args:
        - pattern (str): 模式串

    Returns:
        - List[int]: 前缀表
    """
    size = len(pattern)

    # * 初始化 nexts 数组，nexts[i] 代表位置 i 之前前后缀相同的字符个数
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
    test_str = "aabaabaaf"
    test_pat = "aabaaf"
    main(test_str, test_pat)
