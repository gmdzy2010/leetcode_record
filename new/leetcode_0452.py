from typing import List


def main(points: List[List[int]]):
    """射气球

    Args:
        - points (List[List[int]]): 气球区间
    """
    ans1 = get_min_shots_1(points)
    print(ans1)

    ans2 = get_min_shots_2(points)
    print(ans2)


def get_min_shots_1(points: List[List[int]]) -> int:
    """射气球，按照左边界排序

    Args:
        - points (List[List[int]]): 气球区间

    Returns:
        - int: 需要的箭数量
    """
    size = len(points)
    if size == 0:
        return 0

    # * 气球数量不为零，至少需要一支箭
    ans = 1

    # * 先对区间进行排序，第一排序为左边界
    points.sort(key=lambda x: (x[0], x[1]))

    for i in range(1, size):
        # * 如果相邻两个气球不挨着（上一个点的右边界比当前点的左边界小），需要一支箭
        if points[i - 1][1] < points[i][0]:
            ans += 1

        # ! 如果挨着就将当前点的右边界缩小，相当于将箭射掉的气球移除掉了
        else:
            points[i][1] = min(points[i - 1][1], points[i][1])

    return ans


def get_min_shots_2(points: List[List[int]]) -> int:
    """射气球，按照右边界排序

    Args:
        - points (List[List[int]]): 气球区间

    Returns:
        - int: 需要的箭数量
    """
    size = len(points)
    if size == 0:
        return 0

    # * 气球数量不为零，至少需要一支箭
    ans = 1

    # * 按照右区间由低到高排序
    points.sort(key=lambda x: x[1])

    # * 箭的初始位置在第一个右边界处
    pos = points[0][1]

    for point in points:
        # * 当射箭位置比当前点的左边界小的时候，说明该射箭了
        # ! 因为当前点的左边界和射箭点的右边界重叠
        if pos < point[0]:
            pos = point[1]
            ans += 1

    return ans


if __name__ == "__main__":
    test_nums = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(main(test_nums))
