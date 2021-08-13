from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []
        for i in range(len(nums)):
            n = nums[i]
            while queue and queue[-1] < n:
                queue.pop()
            queue.append(n)
            if i >= k and queue[0] == nums[i-k]:
                queue.popleft()
            if i >= k-1:
                result.append(queue[0])

        return result
