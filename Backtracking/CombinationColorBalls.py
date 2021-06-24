# [Interview Question](https://hackmd.io/EOTMBXzdQSWO8fZz6uUesA)

from typing import List

class Solution:
    def colorBallsCombination(self, balls: List[int], k: int) -> List[List[int]]:
        ans = []

        def helper(start_index, total, comb):
            if (comb[start_index] > balls[start_index]):
                return

            if total == k:
                ans.append(comb[:])
            
            for i in range(start_index, len(balls)): 
                comb[i] += 1
                helper(i, total + 1, comb)
                comb[i] -= 1

        helper(0, 0, [0 for i in range(len(balls))])
        return ans

balls = [3, 2, 5] # [white count, red cound, black count]
k = 4 # choose k balls
s = Solution()
print(s.colorBallsCombination(balls, k))
