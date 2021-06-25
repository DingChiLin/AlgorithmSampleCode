import heapq

class MedianFinder:

    def __init__(self):
        self.largeHeap = []
        self.smallHeap = []

    def addNum(self, num: int) -> None:
        if len(self.smallHeap) == len(self.largeHeap):
            heapq.heappush(self.largeHeap, -heapq.heappushpop(self.smallHeap, -num))
        else:
            heapq.heappush(self.smallHeap, -heapq.heappushpop(self.largeHeap, num))

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            return float(self.largeHeap[0] - self.smallHeap[0]) / 2.0
        else:
            return float(self.largeHeap[0])