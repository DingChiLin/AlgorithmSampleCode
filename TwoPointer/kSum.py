class Sum:
    def two_sum(self, nums, target, start):
        left = start
        right = len(nums) - 1
        res = []
        while left < right:
            val = nums[left] + nums[right]
            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                # remove duplicate
                while left < right and nums[left+1] == nums[left]:
                    left += 1
                left += 1
                right -= 1
        return res

    def k_sum_helper(self, nums, target, k, start):
        if not nums:
            return []
        
        if k == 2:
            return self.two_sum(nums, target, start)

        N = len(nums)
        res = []
        for i in range(start, N):
            if i == start or nums[i] != nums[i-1]:
                for subset in self.k_sum_helper(nums, target - nums[i], k - 1, i + 1):
                    res.append([nums[i]] + subset)
        return res

    def k_sum(self, nums, target, k):
        nums.sort()
        return self.k_sum_helper(nums, target, k, 0)

S = Sum()
nums = [1,0,-1,0,-2,2]
target = 0
k = 4
print(S.k_sum(nums, target, k))