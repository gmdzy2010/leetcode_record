from typing import List


def main(s: List[str]):
    """原地反转字符串，双指针法

    Args:
        - s (List[str]): 原字符串
    """
    L, R = 0, len(s) - 1
    while L < R:
        s[L], s[R] = s[R], s[L]
        L += 1
        R -= 1


if __name__ == "__main__":
    test_strs = ["l", "e", "e", "t"]
    main(test_strs)
    print(test_strs)
