from typing import List


def main(intervals: List[List[int]]) -> int:
    """会议室2，贪心

    Args:
        - intervals (List[List[int]]): 会议起始点

    Returns:
        - int: 最多有几个会议同时进行
    """
    size = len(intervals)

    # * 分别用两个数组保存所有区间起点和终点，并排序
    starts, ends = [i[0] for i in intervals], [i[1] for i in intervals]
    starts.sort()
    ends.sort()

    ans = 0

    # * 同一个时间段有几个会议在进行
    cnt = 0

    # * 用两个指针分别遍历
    i, j = 0, 0
    while i < size and j < size:
        # * 如果当前的开始时间比当前结束时间小，一定有会议进行,
        if starts[i] < ends[j]:
            cnt += 1
            i += 1

        # * 如果开始比结束时间晚，说明有一场会议结束了，会议数量-1
        else:
            cnt -= 1
            j += 1

        # * 每次比较都更新同时进行会议的最大值
        ans = max(ans, cnt)

    return ans


if __name__ == "__main__":
    test_nums = [[0, 30], [5, 10], [15, 20]]
    print(main(test_nums))
