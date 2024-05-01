from math import inf
from typing import List


class MinStack:
    """双栈解法"""

    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int | float] = [inf]

    def push(self, val: int) -> None:
        """入栈

        Args:
            val (int): 待入栈元素
        """
        # * 两个栈的入栈操作保持同时，但是最小栈总是保持入栈之后栈顶是最小值
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        """出栈保持同步"""
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """返回常规栈的头部

        Returns:
            int: 栈顶
        """
        return self.stack[-1]

    def getMin(self) -> int | float:
        """获取最小值

        Returns:
            int | float: 栈的最小值
        """
        return self.min_stack[-1]
