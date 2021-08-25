from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)

s = Solution()
ratings = [1,3,4,5,2]
print(s.candy(ratings))