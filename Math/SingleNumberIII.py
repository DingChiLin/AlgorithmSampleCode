from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:	
        x = 0
        for n in nums:
            x ^= n
        a = 0
        b = 0
        for n in nums:
            if n ^ x > n:
                a ^= n
            else:
                b ^= n
        return [a, b] 
