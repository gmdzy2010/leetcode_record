from typing import List


def main(actions: List[int]) -> List[int]:
    """调整奇偶数顺序，双指针

    Args:
        - actions (List[int]): 原数组

    Returns:
        - List[int]: 调整之后的顺序
    """
    size = len(actions)
    if size <= 2:
        return actions

    i, j = 0, size - 1
    while i < j:
        # * 从头开始找奇数
        while i < j and actions[i] % 2 == 1:
            i += 1

        # * 从尾开始找偶数
        while i < j and actions[j] % 2 == 0:
            j -= 1

        actions[i], actions[j] = actions[j], actions[i]

    return actions


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5]
    print(main(test_nums))
