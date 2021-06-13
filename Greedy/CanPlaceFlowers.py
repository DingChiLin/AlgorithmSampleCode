from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        cnt = 0
        for i in range(N):
            if flowerbed[i] == 0 and \
               (i - 1 < 0 or flowerbed[i - 1] != 1) and \
               (i + 1 == N or flowerbed[i + 1] != 1):
                cnt += 1
                flowerbed[i] = 1
            if cnt >= n:
                return True
        return False

s = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(s.canPlaceFlowers(flowerbed, n))