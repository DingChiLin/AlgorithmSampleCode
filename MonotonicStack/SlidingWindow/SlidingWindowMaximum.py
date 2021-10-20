from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        ans = []
        for i in range(len(nums)):
            n = nums[i]
            while que and nums[que[-1]] < n:
                que.pop()
            que.append(i)
            if que and que[0] <= i-k:
                que.popleft()
            if i >= k-1:
                ans.append(nums[que[0]])
        return ans
