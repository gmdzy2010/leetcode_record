from typing import List


def main(nums: List[int]):
    """寻找峰值，常规

    Args:
        - nums (List[int]): 原数组
    """
    ans1 = find_peak(nums)
    print(ans1)

    ans2 = find_peak_2pointers(nums)
    print(ans2)


def find_peak(nums: List[int]) -> int:
    """寻找峰值，常规

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 峰值元素的任意位置
    """
    size = len(nums)
    for i in range(size):
        existed = True
        if i > 1:
            if nums[i - 1] >= nums[i]:
                existed = False
        if i + 1 < size:
            if nums[i] < nums[i + 1]:
                existed = False

        if existed:
            return i

    return -1


def find_peak_2pointers(nums: List[int]) -> int:
    """寻找峰值，双指针-二分法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 峰值元素的任意位置
    """
    size = len(nums)
    L, R = 0, size - 1
    while L < R:
        M = (L + R) >> 1

        # ! 如果中点值大于其右侧的值，说明当前值有可能是峰值，
        # * 让右边界缩小至当前位置
        if nums[M] > nums[M + 1]:
            R = M
        else:
            L = M + 1

    return R


if __name__ == "__main__":
    test_nums = [1, 2, 1, 3, 5, 6, 4]
    print(main(test_nums))
