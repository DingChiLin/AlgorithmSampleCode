from typing import List
from collections import Counter, defaultdict

class Solution:
    def subarraysWithAtLeastKDistinct(self, nums, k):
        N = len(nums)
        counter = Counter()
        i = 0
        cnt = 0
        for j in range(N):
            counter[nums[j]] += 1
            while len(counter) >= k:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    del counter[nums[i]]
                i += 1
            if len(counter) == k-1:
                cnt += i
        return cnt

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtLeastKDistinct(nums, k) - self.subarraysWithAtLeastKDistinct(nums, k+1)

class Solution2:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = Counter()
        i, j = 0, 0
        ans = 0
        for n in nums:
            counter[n] += 1
            while len(counter) > k:
                counter[nums[j]] -= 1
                if counter[nums[j]] == 0:
                    del counter[nums[j]]
                j += 1
                i = j
            if len(counter) == k:
                while counter[nums[j]] > 1:
                    counter[nums[j]] -= 1
                    j += 1
                ans += (j - i + 1)
        return ans

s = Solution()
nums = [1,2,1,2,3]
k = 2
# nums = [1,2,1,3,4]
# k = 3
print(s.subarraysWithKDistinct(nums, k))