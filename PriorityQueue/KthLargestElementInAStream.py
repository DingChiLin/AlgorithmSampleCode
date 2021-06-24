from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = sorted(nums, reverse = True)[:k]
        heapq.heapify(self.pq)
        print(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]


obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
