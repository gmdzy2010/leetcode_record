from typing import List


def main(nums: List[int], k: int) -> int:
    """和为 K 的子数组，前缀和

    Args:
        - nums (List[int]): 原数组
        - k (int): 目标和

    Returns:
        - int: 和为 K 的子数组的个数
    """
    ans, pre = 0, 0
    cnt = {0: 1}
    for n in nums:
        # * 计算每个位置的前缀和
        pre += n

        # * 说明从某个位置到当前位置的连续子数组的和为k
        # ! 到 i 位置的 前缀和 pre，连续子数组和为 k 的次数 == pre - k 出现的次数
        if pre - k in cnt:
            ans += cnt[pre - k]

        # * 哈希表存储每个前缀和出现的次数
        if pre in cnt:
            cnt[pre] += 1
        else:
            cnt[pre] = 1

    return ans
