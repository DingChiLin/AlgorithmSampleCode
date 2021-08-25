from typing import List
import heapq

# use heap
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        max_heap = []
        min_heap = []
        i = 0
        ans = 0
        for j in range(N):
            n = nums[j]
            heapq.heappush(max_heap, (-n, j))
            heapq.heappush(min_heap, (n, j))
            while (-max_heap[0][0]) - min_heap[0][0] > limit:
                i = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < i:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < i:
                    heapq.heappop(min_heap)
            ans = max(ans, j - i + 1)
        return ans

# use SortedList
from sortedcontainers import SortedList, SortedDict
class Solution2:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        sortedList = SortedList()
        i = 0
        ans = 0
        for j in range(N):
            sortedList.add(nums[j])
            while sortedList and sortedList[-1] - sortedList[0] > limit:
                sortedList.remove(nums[i])
                i += 1
            ans = max(ans, j - i + 1)
        return ans

s = Solution2()
nums = [10,1,2,4,7,2]
limit = 5
print(s.longestSubarray(nums, limit))