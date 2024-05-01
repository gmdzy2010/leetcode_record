from typing import List


def main(s: str, p: str) -> List[int]:
    """字母异位词，数组哈希表法

    Args:
        - s (str): 字符串
        - p (str): 模式串

    Returns:
        - List[int]: 所有 p 的异位词开始的位置列表
    """
    size_s, size_p = len(s), len(p)
    if size_s < size_p:
        return []

    cnt_s, cnt_p, ans = [0] * 26, [0] * 26, []
    for i in range(size_p):
        cnt_s[ord(s[i]) - 97] += 1
        cnt_p[ord(p[i]) - 97] += 1

    if cnt_s == cnt_p:
        ans.append(0)

    for i in range(size_s - size_p):
        cnt_s[ord(s[i]) - 97] -= 1
        cnt_s[ord(s[i + size_p]) - 97] += 1

        if cnt_s == cnt_p:
            ans.append(i + 1)

    return ans


if __name__ == "__main__":
    test_s, test_p = "cbaebabacd", "abc"
    print(main(test_s, test_p))
