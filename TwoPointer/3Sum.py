from typing import List

class Solution:
    # find all possible i, j pairs that:
    #   1. i < j < end
    #   2. nums[i] + nums[j] == target
    def twoSum(self, nums, end, target):
        i = 0
        j = end
        ans = []
        while (i < j):
            tot = nums[i] + nums[j] 
            if tot == target:
                ans.append([i, j])
                i += 1
                j -= 1
            elif tot > target:
                j -= 1
            else:
                i += 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = set()
        for k in range(2, N):
            pairs = self.twoSum(nums, k-1, -nums[k])
            for i, j in pairs:
                ans.add((nums[i], nums[j], nums[k]))
        return [list(t) for t in ans]

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))