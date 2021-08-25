from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        N = len(heights)
        prv = heights[0]
        bricks_sum = 0
        ladders_sum = 0
        ans = 0
        for i in range(1, N):
            h = heights[i]
            diff = h - prv
            if (diff <= 0):
                prv = h
                ans = i 
                continue
                
            bricks_sum += diff
            heapq.heappush(pq, -diff)
            while pq and ladders_sum < ladders and bricks_sum > bricks:
                max_diff = -heapq.heappop(pq)
                bricks_sum -= max_diff
                ladders_sum += 1
            
            if bricks_sum <= bricks:
                ans = i
            else:
                break
            prv = h
        return ans

s = Solution()
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(s.furthestBuilding(heights, bricks, ladders))