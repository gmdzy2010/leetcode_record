from typing import List


def main(arr: List[int | float]) -> List[int | float]:
    """归并排序，时间复杂度O(N * logN)

    Args:
        - arr (List[int | float]): 未排序数组

    Returns:
        - List[int | float]: 已排序数组
    """
    if len(arr) < 2:
        return arr

    process(arr, 0, len(arr) - 1)

    return arr


def process(arr: List[int | float], left_index: int, right_index: int):
    """
    排序处理函数

    分别处理左右两侧，然后合并两侧数组

    Args:
        - arr (List[int | float]): 未排序数组
        - left_index (int): 数组左边界下标
        - right_index (int): 数组右边界下标

    Returns:
        - None
    """
    if left_index == right_index:
        return None

    # middle_index = (right_index + left_index) / 2
    middle_index = left_index + ((right_index - left_index) >> 1)
    process(arr, left_index, middle_index)
    process(arr, middle_index + 1, right_index)
    merge(arr, left_index, middle_index, right_index)

    return None


def merge(
    arr: List[int | float],
    left_index: int,
    middle_index: int,
    right_index: int,
):
    """合并函数

    使用临时存储空间 temp 对数组左半部分 left_part 和右半部分 right_part 进行合并，对两
    部分同时进行遍历，比较当前遍历到的元素：
    - 小的元素先放入 temp, 较小元素所在部分指针前进1
    - 重复这个过程至 left_part 或 right_part 遍历完
    - 由于指针移动速度不一样，会出现两种情况
        - 当 left_part 先遍历完，就把 right_part 剩余部分拷贝至temp
        - 当 right_part 先遍历完，就把 left_part 剩余部分拷贝至temp

    Args:
        - arr (List[int | float]): 未全排序数组
        - left_index (int): 数组左边界下标
        - middle_index (int): 数组中间界下标
        - right_index (int): 数组右边界下标

    Returns:
        - None
    """
    temp: List[int | float] = []
    ptr_l, ptr_r = left_index, middle_index + 1
    while ptr_l <= middle_index and ptr_r <= right_index:
        if arr[ptr_l] <= arr[ptr_r]:
            temp.append(arr[ptr_l])
            ptr_l += 1
        else:
            temp.append(arr[ptr_r])
            ptr_r += 1

    while ptr_l <= middle_index:
        temp.append(arr[ptr_l])
        ptr_l += 1
    while ptr_r <= right_index:
        temp.append(arr[ptr_r])
        ptr_r += 1

    for i, e in enumerate(temp):
        arr[left_index + i] = e


if __name__ == "__main__":
    input_arr = [3, 1, 2, 4, 5, 6, 9, 7, 8]
    print(main(input_arr))
