from typing import List


class MyQueue:
    """用两个栈实现队列"""

    def __init__(self):
        self.stack_in: List[int] = []
        self.stack_out: List[int] = []

    def push(self, x: int) -> None:
        """队列的入队操作

        Args:
            x (int): 待入队元素
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """队列出队操作

        Returns:
            int: 出队元素
        """
        # * 只有 stack_out 为空才会从 stack_in 导入数据
        if not self.stack_out:
            # * 从stack_in 出去的元素全部进入 stack_out，同时也实现了逆序入栈顺序
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        res = self.stack_out.pop()

        return res

    def peek(self) -> int:
        """返回队列头部元素

        Returns:
            int: 头部元素
        """
        res = self.pop()
        self.stack_out.append(res)
        return res

    def empty(self) -> bool:
        """队列是否为空

        Returns:
            bool: 是否为空
        """
        return not self.stack_in and not self.stack_out


if __name__ == "__main__":
    test_queue = MyQueue()
    test_queue.push(2)
    test_queue.push(3)
    test_queue.push(5)
    test_queue.push(9)
    assert test_queue.pop() == 2
    assert test_queue.pop() == 3
    assert test_queue.peek() == 5
    assert test_queue.empty() is False
