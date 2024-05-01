from collections import deque
from typing import Deque


class MyStack1:
    """用一个队列实现栈"""

    def __init__(self):
        self.queue: Deque[int] = deque()

    def push(self, x: int) -> None:
        """入栈

        Args:
            x (int): _description_
        """
        self.queue.appendleft(x)

    def pop(self) -> int:
        """出栈

        Returns:
            int: _description_
        """
        size = len(self.queue)
        for _ in range(1, size):
            self.queue.appendleft(self.queue.pop())

        res = self.queue.pop()

        return res

    def top(self) -> int:
        """栈顶

        Returns:
            int: _description_
        """
        return self.queue[0]

    def empty(self) -> bool:
        """是否栈空

        Returns:
            bool: _description_
        """
        return not self.queue


class MyStack2:
    """用二个队列实现栈"""

    def __init__(self):
        self.queue1: Deque[int] = deque()
        self.queue2: Deque[int] = deque()

    def push(self, x: int) -> None:
        """入栈

        Args:
            x (int): _description_
        """
        # * 元素从队列2入队
        self.queue2.appendleft(x)

        # * 当队列不为空就把队列1中的元素出队列，依次重新在队列2入队，
        # ! 这样保证新入栈的元素始终在原先元素的前面！
        while self.queue1:
            self.queue2.appendleft(self.queue1.pop())

        # * 交换两个队列，因为真正使用的永远是 queue1，正确的顺序在 queue2，换回来
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """出栈

        Returns:
            int: _description_
        """

        return self.queue1.pop()

    def top(self) -> int:
        """栈顶

        Returns:
            int: _description_
        """
        return self.queue1[-1]

    def empty(self) -> bool:
        """是否栈空

        Returns:
            bool: _description_
        """
        return not self.queue1


if __name__ == "__main__":
    test_stack1 = MyStack1()
    test_stack1.push(1)
    test_stack1.push(2)
    test_stack1.push(5)
    test_stack1.pop()
    test_stack1.push(4)
    test_stack1.top()
    test_stack1.empty()

    test_stack = MyStack2()
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(5)
    test_stack.push(4)
    assert test_stack.top() == 4
    assert test_stack.empty() is False
