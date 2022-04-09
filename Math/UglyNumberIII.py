class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def count_ugly(self, target, a, b, c, lcm_ab, lcm_ac, lcm_bc, lcm_abc):
        return target // a + target // b + target // c - target // lcm_ab - target // lcm_ac - target // lcm_bc + target // lcm_abc

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm_ab = a * b // self.gcd(a, b)
        lcm_ac = a * c // self.gcd(a, c)
        lcm_bc = b * c // self.gcd(b, c)
        lcm_abc = a * lcm_bc // self.gcd(a, lcm_bc)
        left = 1
        right = int(2e9)
        
        while left <= right:
            mid = (left + right) // 2
            
            cnt = self.count_ugly(mid, a, b, c, lcm_ab, lcm_ac, lcm_bc, lcm_abc) 
            if cnt >= n:
                right = mid - 1
            else:
                left = mid + 1
            
        return left