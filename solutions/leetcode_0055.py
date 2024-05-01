from typing import List


def main(nums: List[int]) -> bool:
    """跳跃游戏

    Args:
        - nums (List[int]): 原数组

    Returns:
        - bool: 最终能否跳出数组范围
    """
    size = len(nums)
    if size == 1:
        return True

    # * 最大覆盖范围
    cover = 0

    # * 每走一步都更新覆盖范围
    i = 0

    # ! 限制每次只能在 cover 范围内移动，看看最终更新的 cover 会不会比长度大
    while i <= cover:
        # * 当前覆盖范围
        curr_cover = i + nums[i]
        cover = max(curr_cover, cover)

        if cover >= size - 1:
            return True

        i += 1

    return False


if __name__ == "__main__":
    test_nums = [2, 3, 1, 1, 4]
    print(main(test_nums))
