from typing import List


def main(arr: List[int]) -> List[int]:
    """快速排序
    - 时间复杂度：O(N * logN)
    - 空间复杂度：O(N)

    选定最右侧元素作为划分阈值pivot，分别针对 >pivot 和 <=pivot 的元素分区，递归分区至不
    能再分，返回排序数组

    Args:
        - arr (List[int | float]): 未排序数组

    Returns:
        - List[int|float]: 已排序数组
    """
    if len(arr) < 2:
        return arr

    process(arr, 0, len(arr) - 1)

    return arr


def process(arr: List[int], left_index: int, right_index: int):
    """处理函数

    Args:
        - arr (List[int]): 未全排序数组
        - left_index (int): 左边界指针
        - right_index (int): 右边界指针
    """
    if left_index < right_index:
        ptr_p = partition(arr, left_index, right_index)
        process(arr, left_index, ptr_p - 1)
        process(arr, ptr_p + 1, right_index)


def partition(arr: List[int], left_index: int, right_index: int) -> int:
    """分区函数

    获取已分区之后的临界区开始位置

    - 选取当前区域 [left_index, right_index] 的最后一个数作为分区的阈值，随机选择位置更
      好，这样可以防止数据分布影响阈值选择
    - 设定 <pivot 为左半区，左半区指针 ptr_l 初始在 left_index 区域左边的位置
    - 对当前区域元素进行遍历，比较每个元素和阈值的大小
        - 若当前值小于 pivot，左半区指针右移1，交换当前值和左半区指针指向的值
    - 重复上述过程，直到在当前区域完成分区
    - 完成分区后，交换右边界处的值（阈值）和左半区指针下一个位置处的值，形成以下分布
        - | ... < pivot ... | ... = pivot ... | ... > pivot ... |

    Args:
        - arr (List[int]): 未全排序数组
        - left_index (int): 左边界指针
        - right_index (int): 右边界指针

    Returns:
        - int: 临界区开始位置
    """
    # * 出始选择右边界处的值作为划分域值
    pivot = arr[right_index]

    # * <=pivot 区域的边界，初始处于左边界 left_index 左边
    ptr_l = left_index - 1

    # * 依次对左右边界内的元素进行遍历，出现比pivot值小的，就将其移入 <=pivot 区
    for i in range(left_index, right_index):
        if arr[i] <= pivot:
            # 先扩大 <=pivot 区域
            ptr_l += 1

            # 通过交换将当前元素移入 <=pivot 区
            arr[ptr_l], arr[i] = arr[i], arr[ptr_l]

    # * 交换临界区开始位置和右边界位置的值
    arr[ptr_l + 1], arr[right_index] = arr[right_index], arr[ptr_l + 1]

    return ptr_l + 1


if __name__ == "__main__":
    input_arr = [2, 1, 3, 5, 4, 7, 9, 8, 6, 6, 6]
    print(main(input_arr))
