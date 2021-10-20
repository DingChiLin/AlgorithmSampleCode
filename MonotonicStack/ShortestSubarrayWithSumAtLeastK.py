from typing import List
from collections import deque
from math import inf

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        psum = [0] * (N + 1)
        for i in range(N):
            psum[i+1] = psum[i] + nums[i]

        que = deque()
        ans = inf
        for i in range(N+1):
            while que and psum[i] - psum[que[0]] >= k:
                ans = min(ans, i - que[0])
                que.popleft()

            while que and psum[i] < psum[que[-1]]:
                que.pop()

            que.append(i)

        return ans if ans != inf else -1


s = Solution()
nums = [2,-1,2]
k = 3

nums = [1,2]
k = 4

nums = [1]
k = 1
print(s.shortestSubarray(nums, k))