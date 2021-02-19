from collections import deque


class MonoQuene:
    """A simple mono-quene implementation."""
    
    def __init__(self):
        self._quene = deque()
    
    def push(self, value):
        while self._quene and value > self._quene[0]:
            self._quene.popleft()
        self._quene.appendleft(value)
        
    def pop(self, value):
        if self._quene and self._quene[-1] == value:
            self._quene.pop()
    
    def front(self):
        return self._quene[-1]


def max_sliding_window_direct(sequence, k):
    return [max(sequence[i:i + k]) for i in range(len(sequence) - k + 1)]


def max_sliding_window_quene(sequence, k):
    quene, result = MonoQuene(), list()
    for index in range(k):
        quene.push(sequence[index])
    result.append(quene.front())
    for index in range(k, len(sequence)):
        quene.pop(sequence[index - k])
        quene.push(sequence[index])
        result.append(quene.front())
    return result


if __name__ == '__main__':
    test_sequence, test_k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    print(max_sliding_window_direct(test_sequence, test_k))
    print(max_sliding_window_quene(test_sequence, test_k))
