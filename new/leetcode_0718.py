from typing import List


def main(nums1: List[int], nums2: List[int]) -> int:
    """最长连续重复子序列，DP

    Args:
        - nums1 (List[int]): 数组1
        - nums2 (List[int]): 数组2

    Returns:
        - int: 最长连续重复子序列长度
    """
    size_1, size_2 = len(nums1), len(nums2)

    # * dp[i][j] 代表 nums1/nums2 中第 i/j 个元素结尾得到的最长重复子序列
    # ! 显然两个数组都不存在第 0 个元素，约定 dp[i][0]/dp[0][j] 都为 0
    dp = [[0 for _ in range(size_2 + 1)] for _ in range(size_1 + 1)]

    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            # ! 注意这里 dp[i][j] 中的 i/j 和实际的数组索引相差 1
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    return max(map(max, dp))


if __name__ == "__main__":
    test_nums1, test_nums2 = [1, 2, 3, 2, 1], [3, 2, 1, 4, 7]
    print(main(test_nums1, test_nums2))
