from typing import List


def main(nums: List[int]):
    """求数组众数（多数元素）
    - 暴力统计法
    - 哈希统计法
    - 随机化法

    Args:
        - nums (List[int]): _description_
    """
    ans1 = get_mode(nums)
    print(ans1)


def get_mode(nums: List[int]) -> int | None:
    """获取数组众数，哈希表法

    Args:
        - nums (List[int]): 原始数组

    Returns:
        - int | None: 众数
    """
    count_map = {}
    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    size = len(nums)
    for k, v in count_map.items():
        mid = size / 2
        if v > mid:
            return k

    return None


if __name__ == "__main__":
    test_nums = [2, 2, 1, 1, 1, 2, 2]
    main(test_nums)
