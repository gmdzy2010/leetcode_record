from typing import List


def main(nums: List[int]):
    """下一个排列

    - 从后向前查找第一个顺序对 (i, i+1)，满足 a[i] < a[i+1]。这样较小数即为 a[i]
      此时 i+1~n 必然是降序
    - 如果找到了顺序对，那么在区间 i+1~n 中从后向前查找第一个元素 j 满足 a[i] < a[j]。
      这样较大数即为 a[j]
    - 交换 a[i] 与 a[j]，此时区间 i+1~n 必为降序。可以直接反转使其变为升序

    Args:
        - nums (List[int]): 原数组
    """
    size = len(nums)

    # * 先找第一个相邻的升序元素对
    i = size - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # * 在 i+1~n 区域上从后向前查找第一个元素比 i 位置大的元素，然后交换两者
    if i >= 0:
        j = size - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # * 交换过后的 i+1~n 区域为降序，直接逆序将其变成升序排列
    L, R = i + 1, size - 1
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]
        L += 1
        R -= 1


if __name__ == "__main__":
    input_arr = [1, 3, 5, 7]
    main(input_arr)
    print(input_arr)
