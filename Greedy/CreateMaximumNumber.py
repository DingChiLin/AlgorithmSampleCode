from typing import List
from collections import deque

class Solution:
    def maxSingleNums(self, nums, k):
        N = len(nums)
        stk = []
        for i, n in enumerate(nums):
            while stk and (n > stk[-1]) and (len(stk) + (N - i - 1) >= k):
                stk.pop()
            if len(stk) < k:
                stk.append(n)
        return stk

    def merge(self, nums1, nums2):
        res = []
        que1 = deque(nums1)
        que2 = deque(nums2)
        '''
        Note: 
            The comparison condition is different from merge sort here,
            we need to compare the whole remaining array
            hence the time complexity will be theoretically O(N^2).
        '''
        while que1 or que2:
            if que1 > que2:
                res.append(que1.popleft()) 
            else:
                res.append(que2.popleft())
        return res

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = [0] * k
        for i in range(k+1):
            if (i <= len(nums1) and k - i <= len(nums2)):
                s1 = self.maxSingleNums(nums1, i)
                s2 = self.maxSingleNums(nums2, k-i)
                ans = max(ans, self.merge(s1, s2))

        return ans

s = Solution()
nums1 = [6,7]
nums2 = [6,0,4]
k = 5

# nums1 = [2,5,6,4,4,0]
# nums2 = [7,3,8,0,6,5,7,6,2]
# k = 15
print(s.maxNumber(nums1, nums2, k))
