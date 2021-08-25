from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        N = len(capital)
        items = sorted(zip(capital, profits))
        capital = w
        cnt = 0
        i = 0
        heap = []
        while cnt < k:
            while i < N and items[i][0] <= capital:
                heapq.heappush(heap, -items[i][1])
                i += 1
            if not heap:
                break
            capital += (-heapq.heappop(heap))
            cnt += 1 
        return capital

s = Solution()
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(s.findMaximizedCapital(k, w, profits, capital))