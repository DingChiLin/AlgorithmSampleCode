from typing import List

class Solution:
    def maxNumberHelper(self, nums, k):
        N = len(nums)
        stk = []
        for i, n in enumerate(nums):
            while stk and (n > stk[-1]) and (len(stk) + (N - i - 1) >= k):
                stk.pop()
            if len(stk) < k:
                stk.append(n)
        return stk

    def merge(self, nums1, nums2):
        i, j = 0, 0
        res = []
        str1 = "".join([str(x) for x in nums1])
        str2 = "".join([str(x) for x in nums2])
        while i < len(nums1) and j < len(nums2):
            if str1[i:] > str2[j:]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        return res 

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = [0] * k
        for i in range(k+1):
            if (i <= len(nums1) and k - i <= len(nums2)):
                tmp1 = self.maxNumberHelper(nums1, i)
                tmp2 = self.maxNumberHelper(nums2, k-i)
                ans = max(ans, self.merge(tmp1, tmp2))

        return ans

s = Solution()
nums1 = [6,7]
nums2 = [6,0,4]
k = 5

# nums1 = [2,5,6,4,4,0]
# nums2 = [7,3,8,0,6,5,7,6,2]
# k = 15
print(s.maxNumber(nums1, nums2, k))

# print(s.maxNumberHelper([6,1,9,1,1,2], 3))