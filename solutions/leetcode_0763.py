from typing import List


def main(s: str) -> List[int]:
    """划分字母区间，贪心

    Args:
        - s (str): 字符串

    Returns:
        - List[int]: 划分区间后的每个区间长度
    """
    # * 统计每一个字符最后出现的位置
    pos = {c: i for i, c in enumerate(s)}

    start, end, ans = 0, 0, []
    for i, c in enumerate(s):
        end = max(end, pos[c])
        if i == end:
            ans.append(end - start + 1)
            start = i + 1

    return ans


if __name__ == "__main__":
    print(main("ababcbacadefegdehijhklij"))
