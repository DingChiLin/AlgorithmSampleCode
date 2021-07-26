from typing import List

class Solution:
    def splitGroupCount(self, nums, k):
        cnt = 0
        tot = 0
        for n in nums:
            if (tot + n) > k:
                cnt += 1
                tot = n
            else:
                tot += n
        return cnt + 1

    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        while(left < right):
            mid = (left + right) // 2
            if self.splitGroupCount(nums, mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left

s = Solution()
nums = [7,2,5,10,8]
m = 2
print(s.splitArray(nums, m))