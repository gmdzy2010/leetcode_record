from typing import List


def main(nums: List[int]) -> int:
    """最长连续子序列，贪心法（用的双指针）

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 最长连续子序列长度
    """
    size = len(nums)
    ans = 0

    # * 使用两个指针
    p1, p2 = 0, 0
    while p1 < size:
        # * 当前位置比上一个位置小，出现拐点
        # * 将最长连续子序列的起始指针重置为拐点处
        if p1 > 0 and nums[p1] <= nums[p1 - 1]:
            p2 = p1

        # * 下一位置点递增，每次移动 p1，更新最长连续子序列长度
        ans = max(ans, p1 - p2 + 1)

        p1 += 1

    return ans


if __name__ == "__main__":
    test_nums = [1, 3, 5, 4, 7]
    main(test_nums)
