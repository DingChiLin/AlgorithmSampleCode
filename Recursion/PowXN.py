# O(N)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            return x * self.myPow(x, n - 1)

s = Solution()
x = 2.10000
n = 3
print(s.myPow(x, n))