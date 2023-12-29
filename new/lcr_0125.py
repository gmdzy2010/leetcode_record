class CQueue:
    """用两个栈实现队列"""

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        """入队

        Args:
            value (int): _description_
        """
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        """出队

        Returns:
            int: _description_
        """
        if self.stack_out:
            return self.stack_out.pop()

        if not self.stack_in:
            return -1

        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()
