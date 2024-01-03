from typing import List


def main(nums: List[int], val: int) -> int:
    """移除元素，双指针法

    Args:
        - nums (List[int]): 原数组
        - val (int): 待移除的元素

    Returns:
        - int: 移除后的数组长度
    """
    size = len(nums)

    # * 初始让左右两个指针处于数组的左右边界处
    # * 左指针左侧没有 val值，右指针右侧全部为目标值 val
    L, R = 0, size - 1

    while L <= R:
        # * 当左指针处的元素和待删除元素相等，就交换左右边界处的元素
        if nums[L] == val:
            # * 题目允许元素顺序发生改变，所以可以随便换
            nums[L], nums[R] = nums[R], nums[L]

            # * 换完之后 L 相当于回退了一步（左侧的元素换出去了，即少了一个）
            L -= 1

            # * 换完之后 R 左移，因为 R 区域扩大了
            # ! 最终 R 停留在第一个重复元素的前一个位置
            R -= 1

        L += 1

    return R + 1


if __name__ == "__main__":
    test_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    main(test_nums, 2)
