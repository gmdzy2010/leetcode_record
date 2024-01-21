from typing import List


def main(nums1: List[int], nums2: List[int]) -> int:
    """不相交的线，DP-二维

    实际上完全是最长公共子序列（力扣第1143题）的变形

    Args:
        - nums1 (List[int]): 数组1
        - nums2 (List[int]): 数组2

    Returns:
        - int: 不相交的线条数
    """
    size_1, size_2 = len(nums1), len(nums2)

    # * 只要数组元素相等且相对顺序不变就不会相交
    dp = [[0 for _ in range(size_2 + 1)] for _ in range(size_1 + 1)]

    for i in range(1, size_1 + 1):
        for j in range(1, size_2 + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[-1][-1]


if __name__ == "__main__":
    test_nums1, test_nums2 = [1, 2, 4], [1, 4, 2]
    print(main(test_nums1, test_nums2))
