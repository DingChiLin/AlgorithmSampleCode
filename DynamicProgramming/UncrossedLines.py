from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, M+1):
                if nums1[i-1] == nums2[j-1]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])

        return DP[N][M]

s = Solution()
nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]

# nums1 = [1,3,7,1,7,5]
# nums2 = [1,9,2,5,1]
print(s.maxUncrossedLines(nums1, nums2))