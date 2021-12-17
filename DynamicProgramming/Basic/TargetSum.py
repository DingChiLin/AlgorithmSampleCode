from typing import List
from collections import defaultdict

# Knapsack


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        total = sum(nums)
        DP = [[0 for j in range(2*total+2)] for i in range(N+1)] 
        if (target > total):
            return 0
        for i in range(N+1):
            for j in range(2*total+2):
                DP[i][j] = 0
        DP[0][total] = 1
        
        for i in range(1, N+1):
            for j in range(2*total+1):
                n = nums[i-1]
                if (j-n >= 0):
                    DP[i][j] += DP[i-1][j-n]
                
                if (j+n <= 2*total):
                    DP[i][j] += DP[i-1][j+n];  

        return DP[N][total+target]

# Cleaner
class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [defaultdict(int) for i in range(len(nums)+1)]
        dp[0] = {0:1}
        for i in range(1, len(nums) + 1):
            n = nums[i-1]
            for key, value in dp[i-1].items():
                dp[i][key + n] += value
                dp[i][key - n] += value

        return dp[-1][S]

s = Solution()
nums = [1,1,1,1,1]
target = 3
print(s.findTargetSumWays(nums, target))