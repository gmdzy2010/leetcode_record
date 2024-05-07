from typing import List


def main(nums: List[int]) -> int:
    """寻找重复数字，二分法

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 重复的数字
    """
    size = len(nums)
    L, R = 1, size
    while L <= R:
        M = (L + R) // 2
        cnt = 0
        for n in nums:
            if n < M:
                cnt += 1

        if cnt >= M:
            R = M - 1
        else:
            L = M + 1

    return R


if __name__ == "__main__":
    print(main([1, 3, 4, 2, 2]))
