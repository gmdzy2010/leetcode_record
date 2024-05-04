from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_q, size = deque(nums), len(nums)
        for _ in range(k % size):
            nums_q.appendleft(nums_q.pop())

        nums[:] = list(nums_q)
