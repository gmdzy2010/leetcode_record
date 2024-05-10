from typing import List


def main(nums: List[int]) -> int:
    """最长连续数字，哈希表

    Args:
        - nums (List[int]): 原字符串

    Returns:
        - int: 最长连续数字长度
    """
    ans = 0

    # ! 这里必须使用集合，列表的 in 操作会超时
    nums = set(nums)  # type: ignore

    for num in nums:
        # ! 去掉重复的查找
        # * 如果当前数字的前一个数字在集合中，后续的查找一定会包含当前数字
        if num - 1 in nums:
            continue

        curr_num, curr_ans = num, 1

        # * 只要当前数字+1 在集合就一直累加
        while curr_num + 1 in nums:
            curr_num += 1
            curr_ans += 1

        ans = max(ans, curr_ans)

    return ans


if __name__ == "__main__":
    test_nums = [0, 3, 3, 7, 2, 4, 5, 8, 4, 6, 0, 1]
    print(main(test_nums))
