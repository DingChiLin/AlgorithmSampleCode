from math import inf

class Solution:
    def __init__(self):
        self.ans = 0

    def backtracking(self, heights, count, n, m):
        # Pruning
        if count >= self.ans or count > max(n, m):
            return
        
        # Already fill all the rectangle
        if heights[0] == n and len(set(heights)) == 1:
            self.ans = count
            return

        '''
            find left and right indexes of the place with lowest height:

            # #
            # #
            # # o o # #
            # # # # # #

            1. # means the place which has been filled already
            2. o means the place with lowest height   
        '''
        min_height = min(heights)
        left = heights.index(min_height)
        right = left
        while right < m and heights[right] == min_height:
            right += 1

        '''
            find all possible ways to fit a square into the place with lowest height started from bottom-left
            
            1. 
            # #
            # #
            # # 1   # #
            # # # # # #

            2.
            # #
            # # 2 2
            # # 2 2 # #
            # # # # # #
        '''
        for length in range(min(right - left, n - min_height), 0, -1):
            for j in range(left, min(left + length, m)):
                heights[j] += length
            self.backtracking(heights, count + 1, n, m)
            for j in range(left, min(left + length, m)):
                heights[j] -= length

    def tilingRectangle(self, n: int, m: int) -> int:
        self.ans = inf
        self.backtracking([0 for _ in range(m)], 0, n, m)
        return self.ans

s = Solution()
n = 5
m = 8
print(s.tilingRectangle(n, m))