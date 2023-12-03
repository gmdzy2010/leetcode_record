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
    
    def __str__(self):
        return str(self._quene_1)


if __name__ == '__main__':
    test_stack = MyStack()
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    test_stack.push(5)
    test_stack.push(6)
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    print(test_stack.top())
    print(test_stack.empty())
    test_stack.push(7)
    print(test_stack)
