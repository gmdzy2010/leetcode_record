from typing import List


def main(height: List[int]) -> int:
    """盛水最多的容器，双指针

    Args:
        - height (List[int]): 高度列表

    Returns:
        - int: 包含区域的面积
    """
    L, R, ans = 0, len(height) - 1, 0
    while L < R:
        w = R - L
        if height[L] < height[R]:
            h = height[L]
            L += 1
        else:
            h = height[R]
            R -= 1
        ans = max(ans, w * h)

    return ans


if __name__ == "__main__":
    test_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(main(test_heights))
