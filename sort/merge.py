from typing import List


def main(arr: List[int | float]) -> List[int | float]:
    """归并排序
    - 时间复杂度：O(N * logN)
    - 空间复杂度：O(N)

    对数组进行递归二分，再用额外的O(N)空间排序和合并，最终返回已排序的数组

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
        - left_index (int): 数组左边界
        - right_index (int): 数组右边界

    Returns:
        - None
    """
    # * 递归终止条件为左/右边界重合
    if left_index == right_index:
        return None

    # * 下面的两种办法都可以取得中间值，但是位运算更快
    # middle_index = (right_index + left_index) / 2
    middle_index = left_index + ((right_index - left_index) >> 1)

    # * 处理左半部分
    process(arr, left_index, middle_index)

    # * 处理右半部分
    process(arr, middle_index + 1, right_index)

    # * 对处理过的两部分进行合并，合并过程中排序
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
    # * 额外的数组空间，用于合并排序
    temp: List[int | float] = []

    # * 左/右半部分的遍历指针
    ptr_l, ptr_r = left_index, middle_index + 1

    # * 同时对左右部分进行遍历，较小值先放入temp并且指针前进
    while ptr_l <= middle_index and ptr_r <= right_index:
        if arr[ptr_l] <= arr[ptr_r]:
            temp.append(arr[ptr_l])
            ptr_l += 1
        else:
            temp.append(arr[ptr_r])
            ptr_r += 1

    # * 把左/右半部分剩余未参与遍历的元素直接拷贝至temp
    while ptr_l <= middle_index:
        temp.append(arr[ptr_l])
        ptr_l += 1
    while ptr_r <= right_index:
        temp.append(arr[ptr_r])
        ptr_r += 1

    # * 将temp放回原始数组arr
    for i, e in enumerate(temp):
        arr[left_index + i] = e


if __name__ == "__main__":
    input_arr: List[int | float] = [3, 1, 2, 4, 5, 6, 9, 7, 8]
    print(main(input_arr))
