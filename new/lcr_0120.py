from typing import List


def main(nums: List[int]):
    """查找重复元素

    Args:
        - nums (List[int]): 有重复元素的数组
    """
    ans1 = find_repeated_hash(nums)
    print(ans1)

    ans2 = find_repeated_inplace(nums)
    print(ans2)


def find_repeated_hash(nums: List[int]) -> int:
    """查找重复元素，哈希法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 重复元素的位置
    """
    visited = set()
    for i in nums:
        if i in visited:
            return i
        visited.add(i)

    return -1


def find_repeated_inplace(nums: List[int]) -> int:
    """查找重复元素，原地交换法

    本题有一个额外的条件：
    - 在一个长度为 n 的数组内，所有元素的大小满足 0 <= nums[i] <= n - 1

    可以利用这个条件建立哈希数组：
    - 让 0 位置上对应元素 0，1 位置上对应元素 1，...
    - 如果数组中有重复元素，肯定存在两个位置 m 和 n，他们对应的元素是一样的
    - 返回这个元素即可

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 重复元素
    """
    i = 0
    size = len(nums)
    while i < size:
        # * i 位置上的元素和 i 对应上了，说明可以跳过
        if nums[i] == i:
            # ! 这里 i 的自增是被上述条件控制的，说明只要不满足这个条件就得一直交换
            i += 1
            continue

        # * 如果 i 和 nums[i] 位置上的元素相等，说明有重复元素了
        if nums[i] == nums[nums[i]]:
            return nums[i]

        # * 交换 i 位置和 nums[i] 位置上的元素
        # ? 为什么要交换呢？
        # * 因为最终想达到的状态是：对于数组的任意一个位置 k 都有 nums[k] == k
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    return -1


if __name__ == "__main__":
    test_nums = [4, 5, 3, 2, 1, 0, 7, 6, 4]
    main(test_nums)
