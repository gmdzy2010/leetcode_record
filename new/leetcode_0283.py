from typing import List


def main(nums: List[int]):
    """移动零到末尾，双指针法

    使用左右双指针，类似于快排分区的思想
    - 左指针 L 指向当前已处理好序列的尾部，右指针 R 指向待处理序列的头部
        - L 左边均为非零数
        - R 左边直到 L 处均为零
    - R 不断右移，如果 R 处元素非零，则将 L/R 对应的数交换，同时 L 右移

    Args:
        - nums (List[int]): _description_
    """
    size = len(nums)
    if not size:
        return None

    # * 使用两个指针
    L, R = 0, 0
    while R < size:
        # * R 到了不为零的位置，而 L 在第一个为 0 的位置
        if nums[R] != 0:
            # * 交换 L/R 处元素，此时 R 处为 0 ，L不为 0
            nums[L], nums[R] = nums[R], nums[L]

            # * L 右移一步之后，又到了第一个 0 的位置上
            L += 1

        R += 1

    return nums


if __name__ == "__main__":
    test_nums = [1, 0, 1, 0, 3, 12, 5, 0, 8, 4]
    main(test_nums)
