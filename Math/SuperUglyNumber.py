from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pq = []
        N = len(primes)
        for i in range(N):
            heapq.heappush(pq, (primes[i], 1, primes[i]))
            
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1, n):
            dp[i] = pq[0][0]
            while pq and pq[0][0] == dp[i]:
                val, idx, p = heapq.heappop(pq)
                heapq.heappush(pq, (p * dp[idx], idx+1, p))
        return dp[n-1]

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy() # do a deep copy 
        heapq.heapify(nums) #create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums) #take the smallest element
            cnt = 0
            for prime in primes:
                cnt += 1
                heapq.heappush(nums, p * prime) #add all those multiples with the smallest number
                if p % prime == 0:
                    break
        return p

S = Solution()
n = 10000
primes = [2,3,5,7,11,13,17,19]
print(S.nthSuperUglyNumber(n, primes))