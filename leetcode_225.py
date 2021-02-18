from collections import deque


class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._quene_1 = deque()
        self._quene_2 = deque()
    
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._quene_2.append(x)
        while self._quene_1:
            self._quene_2.append(self._quene_1.popleft())
        self._quene_1, self._quene_2 = self._quene_2, self._quene_1
    
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._quene_1.popleft()
    
    def top(self) -> int:
        """
        Get the top element.
        """
        return self._quene_1[0]
    
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self._quene_1
