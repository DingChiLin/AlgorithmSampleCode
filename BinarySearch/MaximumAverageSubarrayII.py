from math import inf

class Solution:
    def search(self, nums, k, x):
        N = len(nums)
        nums = [n - x for n in nums]
        psum = [0] * (N+1)
        for i in range(N):
            psum[i+1] = psum[i] + nums[i]
        
        v = inf
        for i in range(1, N+1):
            if i-k >= 0:
                v = min(v, psum[i-k])
            if psum[i] - v >= 0:
                return True
        return False
        
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = -1e9, 1e9
        while (left + 1e-6 < right):
            mid = (left + right) / 2
            if self.search(nums, k, mid):
                left = mid 
            else:
                right = mid
        return left