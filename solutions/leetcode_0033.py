from typing import List


def main(nums: List[int], target: int) -> int:
    """搜索旋转排序数组

    使用二分法查找即可

    二分法搜索的前提是有序，但是经过旋转之后的数组已经不是全局有序，但是每次二分有一定有一个
    局部有序的区间，可以利用这个性质使用二分查找加速搜索过程

    旋转后的数组存在三个特点：
    - 只有在有序区间内才可以通过区间两端的数值判断 target 是否在其中
    - 判断顺序区间还是乱序区间，只需要对比左边界 L 和右边界 R 处是否是顺序对即可，
        - nums[L] <= nums[R]：顺序区间
        - nums[L] <= nums[R]：乱序区间
    - 每次二分都会至少存在一个顺序区间

    Args:
        - nums (List[int]): 旋转过的数组
        - target (int): 要搜索的值

    Returns:
        - int: 搜索值的位置
    """
    if not nums:
        return -1

    size = len(nums)
    L, R = 0, size - 1
    while L <= R:
        # * 确定中间点位置
        M = (L + R) // 2
        if nums[M] == target:
            return M

        # * 根据 nums[L] 和 nums[M] 的值来确定二分的边界，存在两种不同的情况
        # ! 注意这里必须是小于等于，否则会有一些边界情况失效
        if nums[L] <= nums[M]:
            # * target 在左半区，M - 1 <- R
            if nums[L] <= target < nums[M]:
                R = M - 1

            # * target 在右半区，L -> M + 1
            else:
                L = M + 1

        # * 右半区是顺序区间，同理
        else:
            if nums[M] < target <= nums[R]:
                L = M + 1
            else:
                R = M - 1

    return -1


if __name__ == "__main__":
    input_nums = [4, 5, 6, 7, 8, 9, 11, 14, 0, 1, 2, 3]
    print(main(input_nums, 1))
