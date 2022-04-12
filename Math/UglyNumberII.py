class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        id2 = 1
        id3 = 1
        id5 = 1
        cnt = 1
        while cnt < n:
            nxt = min(dp[id2] * 2, dp[id3] * 3, dp[id5] * 5)
            if nxt == dp[id2] * 2:
                id2 += 1
            if nxt == dp[id3] * 3:
                id3 += 1
            if nxt == dp[id5] * 5:
                id5 += 1
            cnt += 1
            dp[cnt] = nxt
        return dp[n]

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = [1]
        ans = 0
        visited = set([1])
        for i in range(n):
            num = heapq.heappop(pq)
            ans = num
            for k in [2,3,5]:
                if num*k not in visited:
                    visited.add(num*k)
                    heapq.heappush(pq, num*k)
        return ans