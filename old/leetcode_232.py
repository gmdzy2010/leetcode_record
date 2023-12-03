class MyQueue:
    """A simple quene implementation using list(stack). """
    
    def __init__(self):
        """Initialize your data structure here."""
        self._input_stack = []
        self._output_stack = []
        self._front = None
    
    def push(self, x):
        """Push element x to the back of queue."""
        if not self._input_stack:
            self._front = x
        self._input_stack.append(x)
    
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._output_stack:
            while self._input_stack:
                self._output_stack.append(self._input_stack.pop())
        return self._output_stack.pop()
    
    def peek(self):
        """Get the front element."""
        if self._output_stack:
            return self._output_stack[-1]
        return self._front
    
    def empty(self):
        """Returns whether the queue is empty."""
        if not self._input_stack and not self._output_stack:
            return True
        return False


if __name__ == '__main__':
    test_quene = MyQueue()
    test_quene.push(2)
    test_quene.push(3)
    test_quene.push(4)
    test_quene.push(7)
    test_quene.push(9)
    test_quene.pop()
    test_quene.push(3)
