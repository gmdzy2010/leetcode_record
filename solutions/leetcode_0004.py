from typing import List


def main(nums1: List[int], nums2: List[int]) -> float:
    """寻找两个正序数组的中位数，二分法

    Args:
        - nums1 (List[int]): 数组1
        - nums2 (List[int]): 数组2

    Returns:
        - float: 目标中位数
    """
    size_1, size_2 = len(nums1), len(nums2)
    if size_1 > size_2:
        return main(nums2, nums1)

    # * 两个数组合并在一起后的中间位置
    # ? 为什么要 +1 ?
    M_total = (size_1 + size_2 + 1) // 2

    # * 用二分法确定总数组左半侧在两个数组中分别取了多少数字
    L, R = 0, size_1
    while L < R:
        # * 数组1的中间位置
        M = (L + R) // 2

        # * 总数组和数组1的中间位置差值
        M_delta = M_total - M

        # * 如果数组1的中位数比数组2的 M_delta-1 位置小，显然
        if nums1[M] < nums2[M_delta - 1]:
            L = M + 1
        else:
            R = M

    # * nums1[M] 为总数组在 nums1 中取的最后一个数字
    # * 显然总数组中位数前面的剩余部分都是从 nums2 中取的
    M, M_delta = L, M_total - L

    if M == 0:
        m1 = nums2[M_delta - 1]
    elif M_delta == 0:
        m1 = nums1[M - 1]
    else:
        m1 = max(nums1[M - 1], nums2[M_delta - 1])

    if (size_1 + size_2) % 2 == 1:
        return m1

    if M == size_1:
        m2 = nums2[M_delta]
    elif M_delta == size_2:
        m2 = nums1[M]
    else:
        m2 = min(nums1[M], nums2[M_delta])

    return (m1 + m2) / 2


if __name__ == "__main__":
    nums1 = [-1, 1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8, 10, 12, 14, 16]
    nums_total = nums1 + nums2
    nums_total.sort()
    print(nums_total)
    print(main(nums1, nums2))
