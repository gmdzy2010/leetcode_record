from typing import List


def main(nums: List[int]) -> None:
    """颜色分类，原地交换法

    Args:
        - nums (List[int]): 颜色数组
    """
    size = len(nums)
    if size < 2:
        return

    i_0, i, i_2 = 0, 0, size
    while i < i_2:
        if nums[i] == 0:
            nums[i], nums[i_0] = nums[i_0], nums[i]
            i += 1
            i_0 += 1
        elif nums[i] == 1:
            i += 1
        else:
            i_2 -= 1
            nums[i], nums[i_2] = nums[i_2], nums[i]


if __name__ == "__main__":
    main([2, 0, 2, 1, 1, 2])
