from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]

s = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums, k))