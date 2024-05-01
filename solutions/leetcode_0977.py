from typing import List


def main(nums: List[int]) -> List[int]:
    """有序数组的平方，双指针法

    Args:
        - nums (List[int]): 有序数组

    Returns:
        - List[int]: 每个元素平方且排序后的数组
    """
    size = len(nums)
    ans = [0] * size

    # * 在左右边界处分别使用一个指针
    L, R = 0, size - 1

    # * 记录结果也用一个指针，结果逆序放入
    curr = size - 1
    while L <= R:
        # * 因为数组 nums 已经按照升序排序，平方后最大数只可能在左右边界处
        # * 左右边界处哪个值大，就倒着填写进结果数组即可
        L_square, R_square = nums[L] * nums[L], nums[R] * nums[R]
        if L_square > R_square:
            ans[curr] = L_square
            L += 1
        else:
            ans[curr] = R_square
            R -= 1

        curr -= 1

    return ans


if __name__ == "__main__":
    test_nums = [-7, -4, -1, 0, 1, 2, 3, 5, 10]
    main(test_nums)
