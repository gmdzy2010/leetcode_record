from typing import List


def main(nums: List[int]) -> List[List[int]]:
    """在数组中找到三数之和为0的所有组合，结果不重复

    排序结合双指针
    - 先对数组进行排序


    Args:
        nums (List[int]): 原数组

    Returns:
        List[List[int]]: 符合条件的三数组合列表
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
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # * 使用 L/R 两个指针分别从数组左右侧走
        L = i + 1
        R = size - 1
        while L < R:
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
