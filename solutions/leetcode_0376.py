from typing import List


def main(nums: List[int]) -> int:
    """摆动数组

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 最大峰值个数
    """
    size = len(nums)
    if not size:
        return size

    # * 初始峰值个数为 1
    ans = 1

    # * 当前数字和前一个数字的差值
    prev_diff = 0

    # * 下一个数字和当前数字的差值
    curr_diff = 0

    # * 记得遍历的时候最后一个位置不取
    for i in range(size - 1):
        curr_diff = nums[i + 1] - nums[i]

        # ! 注意这里的条件，因为每次遍历结束都会把前一个差值更新为现有差值
        if (prev_diff <= 0 and curr_diff > 0) or (
            prev_diff >= 0 and curr_diff < 0
        ):
            ans += 1
            prev_diff = curr_diff

    return ans


if __name__ == "__main__":
    test_nums = [1, 7, 4, 9, 2, 5]
    print(main(test_nums))
