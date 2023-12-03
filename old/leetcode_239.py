from collections import deque


def max_sliding_window_direct(sequence, k):
    return [max(sequence[i:i + k]) for i in range(len(sequence) - k + 1)]


class MonoQuene:
    """A simple mono-quene implementation."""
    
    def __init__(self):
        self.quene = deque()
    
    def push(self, value):
        # the front of the mono-quene should always be the largest one.
        # So all of the elements smaller than the pushed value should be pop
        # out on the left.
        while self.quene and value > self.quene[0]:
            self.quene.popleft()
        self.quene.appendleft(value)
    
    def pop(self, value):
        # The quene just need pop out the element which value equals to the
        # last element removed from the sliding window.
        if self.quene and self.quene[-1] == value:
            self.quene.pop()
    
    def front(self):
        return self.quene[-1]
    
    def __str__(self):
        return str(self.quene)


def max_sliding_window_quene(sequence, k):
    quene, result = MonoQuene(), list()
    
    # Initialize the quene
    for index in range(k):
        quene.push(sequence[index])
    result.append(quene.front())
    
    # the window should start to slide at index k.
    for index in range(k, len(sequence)):
        quene.pop(sequence[index - k])
        quene.push(sequence[index])
        result.append(quene.front())
    return result


if __name__ == '__main__':
    test_sequence, test_k = [1, 3, -1, -3, 5, 3, 3, 6, 7], 3
    print(max_sliding_window_direct(test_sequence, test_k))
    print(max_sliding_window_quene(test_sequence, test_k))
