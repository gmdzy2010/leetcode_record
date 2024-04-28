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
        pre += n
        if pre - k in cnt:
            ans += cnt[pre - k]

        if pre in cnt:
            cnt[pre] += 1
        else:
            cnt[pre] = 1

    return ans
