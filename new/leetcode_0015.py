from typing import List


def main(nums: List[int]) -> List[List[int]]:
    """在数组中找到三数之和为0的所有组合，结果不重复

    排序结合双指针
    - 先对数组进行排序
    - 对排过序的数组进行循环，外层使用一个指针，内层使用左右两个指针分别从两侧相向走
        - 当外层指针和内层的两个指针处元素和为0时
            - 记下该组合
            - 检查左/右指针的下一个位置是否和当前元素相等，相等就再向右/左走一步
            - 左/右指针向右/左走一步
        - 当外层指针和内层左右指针处元素和大于零，由于数组的单调性，让右指针往回走一步
        - 当外层指针和内层左右指针处元素和小于零，由于数组的单调性，让左指针向前走一步
    - 重复执行上述过程即获得答案

    Args:
        - nums (List[int]): 原数组

    Returns:
        - List[List[int]]: 符合条件的三数组合列表
    """
    result: List[List[int]] = []
    size = len(nums)
    if not nums or size < 3:
        return result

    # * 数组排序，对后续跳过重复组合做准备
    nums.sort()

    for i in range(size):
        if nums[i] > 0:
            return result

        # * 检查当前元素和上一个元素是否相同，相同就跳过
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # * 使用 L/R 两个指针分别从数组左/右侧相向而行，直到相遇
        L = i + 1
        R = size - 1
        while L < R:
            # * 三数之和为零，L/R 同时向前走
            if nums[i] + nums[L] + nums[R] == 0:
                result.append([nums[i], nums[L], nums[R]])

                # * 去除左右指针和其下一轮循环值相等的情况
                while L < R and nums[L] == nums[L + 1]:
                    L += 1
                while L < R and nums[R] == nums[R - 1]:
                    R -= 1

                L += 1
                R -= 1

            # * 三数之和大于零，右指针往回走
            elif nums[i] + nums[L] + nums[R] > 0:
                R -= 1

            # * 剩余情况左指针向前走
            else:
                L += 1

    return result


if __name__ == "__main__":
    input_arr = [-1, 0, 1, 2, -1, -4]
    print(main(input_arr))
