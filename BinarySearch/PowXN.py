# Exponentiating by squaring O(logN) 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = (n >= 0)
        n = abs(n)
        ans = 1
        cur = x
        while(n > 0):
            if (n % 2 == 1):
                ans *= cur
            cur *= cur
            n //= 2
        return ans if sign else 1/ans

# Exponentiating by squaring + bit operation O(logN) 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = (n >= 0)
        n = abs(n)
        ans = 1
        cur = x
        while(n > 0):
            if (n & 1):
                ans *= cur
            cur *= cur
            n >>= 1
        return ans if sign else 1/ans

s = Solution()
x = 2.10000
n = 3
x = 2.00000
n = -2
print(s.myPow(x, n))