from collections import deque
from typing import Deque, List


class MonoQueue:
    """单调队列（从左到右单调递增）"""

    def __init__(self):
        self.queue: Deque[int] = deque()

    def push(self, val: int):
        """入队

        入队的时候检查入队元素是否比最左边的元素大
        - 如果比最左边的元素大，就将最左边的元素出队列，再将此元素左边入队
        - 重复上述过程

        这样如果当前元素比队列中的所有元素都大，入队操作后，队列中就只有当前元素的值

        Args:
            - val (int): 待入队元素
        """
        while self.queue and val > self.queue[0]:
            self.queue.popleft()
        self.queue.appendleft(val)

    def pop(self, val: int):
        """出队

        出队操作保证滑动窗口移动的时候，一定保证不在窗口中的元素不会干扰结果

        Args:
            - val (int): 待出队元素
        """
        if self.queue and val == self.queue[-1]:
            self.queue.pop()

    def get_max(self) -> int:
        """获取队列最大值

        最大值就是队列最右边

        Returns:
            - int: 最大值
        """
        return self.queue[-1]


def get_max_within_sliding_window(nums: List[int], k: int) -> List[int]:
    """滑动窗口最大值

    Args:
        - nums (List[int]): 数组
        - k (int): 滑动窗口大小

    Returns:
        List[int]: 最大值列表
    """
    mono_q: MonoQueue = MonoQueue()
    ans: List[int] = []

    # * 先将前k个元素入队
    for i in range(k):
        mono_q.push(nums[i])

    ans.append(mono_q.get_max())

    size = len(nums)
    for i in range(k, size):
        # * 尝试从队列中移除
        mono_q.pop(nums[i - k])
        mono_q.push(nums[i])
        ans.append(mono_q.get_max())

    return ans


if __name__ == "__main__":
    test_nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(get_max_within_sliding_window(test_nums, 3))
