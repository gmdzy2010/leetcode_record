from typing import Dict, List


def main(
    nums1: List[int],
    nums2: List[int],
    nums3: List[int],
    nums4: List[int],
) -> int:
    """四数相加

    Args:
        - nums1 (List[int]): 数组1
        - nums2 (List[int]): 数组2
        - nums3 (List[int]): 数组3
        - nums4 (List[int]): 数组4

    Returns:
        - int: 四数之和为0的组合个数
    """
    visited: Dict[int, int] = {}
    ans = 0

    for n1 in nums1:
        for n2 in nums2:
            total = n1 + n2
            visited[total] = 1 if total not in visited else visited[total] + 1

    for n3 in nums3:
        for n4 in nums4:
            remain = 0 - n3 - n4
            if remain in visited:
                ans += visited[remain]

    return ans


if __name__ == "__main__":
    test_nums1 = [1, 2]
    test_nums2 = [-1, -2]
    test_nums3 = [1, -2]
    test_nums4 = [-1, 2]
    print(main(test_nums1, test_nums2, test_nums3, test_nums4))
