from heapq import heappop, heappush


class MedianFinder:
    """数据流中位数"""

    def __init__(self):
        # * 小根堆
        self.A = []

        # * 大根堆
        self.B = []

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        if len(self.A) != len(self.B):
            return self.A[0]
        else:
            return (self.A[0] - self.B[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.findMedian()

    mf.addNum(3)
    mf.findMedian()
