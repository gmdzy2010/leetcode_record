from typing import List, Set


def main(nums: List[int]):
    """三数之和，双指针法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - List[List[int]]: 符合条件的三数组合列表
    """
    ans1 = three_sum_2pointers(nums)
    print(ans1)

    ans2 = three_sum_hashmap(nums)
    print(ans2)


def three_sum_2pointers(nums: List[int]) -> List[List[int]]:
    """三数之和，双指针法

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
        # ! i 固定为最左侧的数，而 num[i] <= nums[L] <= nums[R]，nums[i] 大于零，
        # ! 三数之和必然大于零
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


def three_sum_hashmap(nums: List[int]) -> List[List[int]]:
    """三数之和，哈希表法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - List[List[int]]: 符合条件的三数组合列表
    """
    ans: List[List[int]] = []

    # * 一定要先排序
    nums.sort()

    size = len(nums)
    for i in range(size):
        if nums[i] > 0:
            break

        # * 相邻数字重复去重
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        visited: Set[int] = set()
        for j in range(i + 1, size):
            # * 相邻两位相同去重
            # ? 这是为什么
            if j > i + 2 and nums[j - 2] == nums[j - 1] and nums[j - 1] == nums[j]:
                continue

            c = 0 - nums[i] - nums[j]
            if c in visited:
                ans.append([nums[i], nums[j], c])
                visited.remove(c)
            else:
                visited.add(nums[j])

    return ans


if __name__ == "__main__":
    test_nums = [-1, 0, 1, 2, -1, -4]
    main(test_nums)
