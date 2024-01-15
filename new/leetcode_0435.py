from typing import List


def main(intervals: List[List[int]]) -> int:
    """无重叠区间，贪心

    Args:
        - intervals (List[List[int]]): 所有区间

    Returns:
        - int: 删除的区间个数
    """
    size = len(intervals)
    if size == 0:
        return 0

    # * 按照右边界排序
    intervals.sort(key=lambda x: x[1])

    # * 初始已经有一个区间
    ans = 1

    # * 排序后放到第一个右边界处
    pos = intervals[0][1]

    # * 遍历所有区间，统计所有不重叠的区间
    for i in range(size):
        # * 只要第一个右边界比左边界小，说明不重叠
        if pos <= intervals[i][0]:
            ans += 1
            pos = intervals[i][1]

    return size - ans


if __name__ == "__main__":
    test_nums = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(main(test_nums))
