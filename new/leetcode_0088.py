from typing import List


def merge_normal_2pointers(
    nums1: List[int],
    m: int,
    nums2: List[int],
    n: int,
):
    """原地合并两个有序数组，正向双指针法

    Args:
        - nums1 (List[int]): 有序数组1
        - m (int): 有序数组1大小
        - nums2 (List[int]): 有序数组2
        - n (int): 有序数组2大小
    """
    if not nums1 or not nums2:
        return nums1 + nums2

    merged = []
    i1, i2 = 0, 0
    while i1 < m or i2 < n:
        # ! 先判断指针越界的2种情况
        # * 如果到达 nums1 的尾部，i1 停止移动，i2 继续
        if i1 == m:
            merged.append(nums2[i2])
            i2 += 1

        # * 如果到达 nums2 的尾部，i2 停止移动，i1 继续
        elif i2 == n:
            merged.append(nums1[i1])
            i1 += 1

        # * 数组不越界的情况下，哪个小就先要哪个
        elif nums1[i1] < nums2[i2]:
            merged.append(nums1[i1])
            i1 += 1
        else:
            merged.append(nums2[i2])
            i2 += 1

    nums1[:] = merged

    return nums1


def merge_reversed_2pointers(
    nums1: List[int],
    m: int,
    nums2: List[int],
    n: int,
):
    """原地合并两个有序数组，逆向双指针法

    Args:
        - nums1 (List[int]): 有序数组1
        - m (int): 有序数组1大小
        - nums2 (List[int]): 有序数组2
        - n (int): 有序数组2大小
    """
    # * 使用两个指针，分别从两个数组的尾部往前遍历
    i1, i2 = m - 1, n - 1

    # * 合并后的数组尾部指针的位置
    merged_tail_i = m + n - 1

    while i1 >= 0 or i2 >= 0:
        # * 先到达 num1 的头部，那么 i1 停止移动，后续只有 i2 往前移动
        if i1 == -1:
            nums1[merged_tail_i] = nums2[i2]
            i2 -= 1

        # * 先到达 num2 的头部，那么 i2 停止移动，后续只有 i1 往前移动
        elif i2 == -1:
            nums1[merged_tail_i] = nums2[i1]
            i1 -= 1

        # * 哪个小要哪个，指针移动哪个
        elif nums1[i1] > nums2[i2]:
            nums1[merged_tail_i] = nums1[i1]
            i1 -= 1
        else:
            nums1[merged_tail_i] = nums2[i2]
            i2 -= 1

        merged_tail_i -= 1
