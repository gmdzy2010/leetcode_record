from typing import List


def main(nums: List[int]) -> int:
    """跳跃游戏2，贪心

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 达到数组长度最小步数
    """
    size = len(nums)

    # * 初始在 0 位置，肯定得跳一步
    ans = 0

    # * 当前能到达的最远位置
    curr_max_i = 0

    # * 下一步能到达的最远位置
    next_max_i = 0

    i = 0
    while i < size:
        # * 记录走过的位置 i 中到达最远位置，最终就能步数最少
        next_max_i = max(i + nums[i], next_max_i)

        # * 到了最远位置（不得不跳）时跳一步
        if i == curr_max_i:
            # * 如果当前最远位置恰好是终点，不用跳了，跳出循环
            if curr_max_i == size - 1:
                break

            # * 跳一步
            ans += 1

            # * 更新当前能到的最远距离
            curr_max_i = next_max_i

            # * 如果下一个位置已经到了或者超过了终点，停止循环
            if next_max_i >= size - 1:
                break

        i += 1

    return ans


if __name__ == "__main__":
    test_nums = [2, 3, 1, 1, 4]
    print(main(test_nums))
