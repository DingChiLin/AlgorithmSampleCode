class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 2**31
        while left + 0.0000001 < right:
            mid = (left + right) / 2
            if mid * mid > x:
                right = mid
            else:
                left = mid 
        return int(left + 0.0000001)