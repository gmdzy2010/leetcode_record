from typing import List, Set


def main(nums1: List[int], nums2: List[int]) -> List[int]:
    """两个数组交集

    Args:
        - nums1 (List[int]): 数组1
        - nums2 (List[int]): 数组2

    Returns:
        - List[int]: 两个数组交集
    """
    ans: Set[int] = set()
    for num in nums2:
        if num in nums1:
            ans.add(num)

    return list(ans)


if __name__ == "__main__":
    test_n1, test_n2 = [1, 2, 3, 3], [1, 3, 3]
    print(main(test_n1, test_n2))
