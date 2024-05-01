from typing import List


def main(intervals: List[List[int]]) -> List[List[int]]:
    """合并区间，贪心

    Args:
        - intervals (List[List[int]]): 原区间列表

    Returns:
        - List[List[int]]: 合并后的区间列表
    """
    # * 按左边界排序
    intervals.sort(key=lambda x: x[0])

    ans: List[List[int]] = []
    for interval in intervals:
        # * 如果合并后的区间列表为空，或者上一个区间右边界比当前区间左边界小（没有重叠）
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)

        # * 有重叠，就鼻尖上一个右边界和当前右边界哪个更靠右，就取哪个
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans


if __name__ == "__main__":
    test_nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(main(test_nums))
