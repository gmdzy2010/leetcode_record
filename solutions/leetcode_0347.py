from heapq import heappop, heappush
from typing import Dict, List, Tuple


def main(nums: List[int], k: int) -> List[int]:
    """前K个高频元素，优先级队列

    Args:
        - nums (List[int]): 原数组
        - k (int): 高频元素个数

    Returns:
        - List[int]: 前K个高频元素
    """
    # * 使用哈希表统计每个数字出现的次数
    counts: Dict[int, int] = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    # * 使用优先级队列得到前k个高频元素
    pq: List[Tuple[int, int]] = []
    for n, c in counts.items():
        heappush(pq, (c, n))

        # ! 始终保持队列中只有K个元素
        if len(pq) > k:
            heappop(pq)

    ans = [heappop(pq)[1] for _ in range(k)]

    return ans


if __name__ == "__main__":
    test_nums = [1, 1, 1, 2, 2, 3]
    print(main(test_nums, 2))
