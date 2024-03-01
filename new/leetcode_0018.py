from typing import List


def main(nums: List[int], target: int) -> List[List[int]]:
    """四数之和，双指针法

    Args:
        - nums (List[int]): 原始数组
        - target (int): 目标和

    Returns:
        - List[List[int]]: 符合条件的结果
    """
    ans: List[List[int]] = []

    # * 排序是重中之重
    nums.sort()

    size = len(nums)
    for i in range(size):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        for j in range(i + 1, size):
            if j > i + 1 and nums[j - 1] == nums[j]:
                continue

            # * 从当前位置的下一个位置开始，双指针找符合条件的剩余两个数字
            L, R = j + 1, size - 1
            while L < R:
                remain = nums[L] + nums[R]
                if nums[i] + nums[j] > target - remain:
                    R -= 1
                elif nums[i] + nums[j] < target - remain:
                    L += 1
                else:
                    ans.append([nums[i], nums[j], nums[L], nums[R]])

                    # * 找到一个四元组后，去重
                    while L < R and nums[R - 1] == nums[R]:
                        R -= 1
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1

                    # * 左右同时向内收缩
                    L += 1
                    R -= 1

    return ans


if __name__ == "__main__":
    test_nums = [1, 0, -1, 0, -2, 2]
    print(main(test_nums, 0))
