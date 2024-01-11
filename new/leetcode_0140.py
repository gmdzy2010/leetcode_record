from typing import List


def main(s: str, wordDict: List[str]) -> List[str]:
    """单词拆分，回溯法

    Args:
        - s (str): 原字符串
        - wordDict (List[str]): 备选单词列表

    Returns:
        - List[str]: 全部符合条件的句子列表
    """
    res: List[str] = []
    ans: List[str] = []

    backtracking(s, 0, wordDict, res, ans)

    return ans


def backtracking(
    s: str,
    start: int,
    words: List[str],
    res: List[str],
    ans: List[str],
):
    """回溯函数

    Args:
        - s (str): 原字符串
        - start (int): 字符串开始匹配位置
        - words (List[str]): 备选单词列表
        - res (List[str]): 符合条件的单词列表
        - ans (List[str]): 全部符合条件的句子列表
    """
    # * 长度达到字符串长度即可停止循环
    if len("".join(res)) == len(s):
        ans.append(" ".join(res))
        return

    # * 备选列表中的单词每次都可以重复选取，所以每次递归都从 0 开始
    for w in words:
        step = len(w)

        # * 当s相应的位置和待选单词相同时，继续向后寻找
        if s[start : start + step] == w:
            res.append(w)

            backtracking(s, start + step, words, res, ans)

            res.pop()


if __name__ == "__main__":
    test_str, test_words = "catsanddog", ["cat", "cats", "and", "sand", "dog"]
    print(main(test_str, test_words))
