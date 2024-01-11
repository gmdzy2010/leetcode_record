from typing import List, Set


def main(s: str, wordDict: List[str]):
    """单词拆分

    Args:
        - s (str): 原字符串
        - wordDict (List[str]): 备选单词列表

    Returns:
        - bool: 是否找到了单词
    """

    # * 常规的回溯，会超时
    ans1 = backtracking(s, 0, wordDict, [])
    print(ans1)

    # * 记忆化搜索
    memory = [1] * len(s)
    words = set(wordDict)
    ans2 = backtracking_memory(s, 0, words, memory)
    print(ans2)


def backtracking(s: str, start: int, words: List[str], res: List[str]) -> bool:
    """回溯递归函数

    Args:
        - s (str): 原字符串
        - start (int): 开始位置
        - words (List[str]): 备选单词列表
        - res (List[str]): 结果

    Returns:
        - bool: 是否找到了单词
    """
    if "".join(res) == s:
        return True

    for w in words:
        step = len(w)
        if s[start : start + step] == w:
            res.append(w)

            # * 如果后续的匹配返回true，说明匹配上了
            if backtracking(s, start + step, words, res):
                return True

            res.pop()

    return False


def backtracking_memory(
    s: str,
    start: int,
    words: Set[str],
    memory: List[int],
) -> bool:
    """回溯递归函数

    Args:
        - s (str): 原字符串
        - start (int): 开始位置
        - words (Set[str]): 备选单词集合
        - memory (List[int]): s 从每个位置 i 开始到最后的区间无法匹配

    Returns:
        - bool: s 是否可以拆分成备选单词集合
    """
    size = len(s)
    if start >= size:
        return True

    # * 如果当前位置的标记为 -1， 说明 s 的 (start, size) 区间无法拆成备选单词集合
    if memory[start] == -1:
        return False

    for i in range(start, size):
        # * 跳过无法拆分出备选单词的位置
        if s[start : i + 1] not in words:
            continue

        # * 此时 s 拆分出了集合中的某个单词 s，继续向后面递归查找
        if backtracking_memory(s, i + 1, words, memory):
            return True

    # * 找遍了 (start, size) 也没能拆成备选单词集合，
    # ! 记住这次尝试：当前位置开始就拆不出来了
    memory[start] = -1

    return False


if __name__ == "__main__":
    test_str, test_words = "applepenapple", ["apple", "pe"]
    main(test_str, test_words)
