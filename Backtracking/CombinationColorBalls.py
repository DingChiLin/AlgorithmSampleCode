# [Interview Question](https://hackmd.io/EOTMBXzdQSWO8fZz6uUesA)

from typing import List

# Like N Digit Password
class Solution:
    def __init__(self):
        self.ans = []
    
    def find(self, depth: int, max_depth: int, balls: List[int], k: int, comb: List[int]):
        if depth == max_depth:
            if k == 0:
                self.ans.append(comb[:])
            return

        for i in range(balls[depth] + 1):
            if i <= k:
                comb.append(i)
                self.find(depth + 1, max_depth, balls, k - i, comb)
                comb.pop()

    def colorBallsCombination(self, balls: List[int], k: int):
        self.ans = []
        self.find(0, len(balls), balls, k, [])
        return self.ans

# Add balls one by one
class Solution2:
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
