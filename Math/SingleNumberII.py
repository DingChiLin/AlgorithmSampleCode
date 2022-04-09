'''
b n    b c
0 0    0 0
0 1 => 1 0
1 0    1 0
1 1    0 1

a c     a  
0 0     0
0 1  => 1
1 0     1
1 1     0

a b    a b
0 0    0 0
0 1 => 0 1
1 0    1 0
1 1    0 0

a b    a ^ b
0 0      0
0 1 =>   1 
1 0      1
1 1      0
'''

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for n in nums:
            b, c = b ^ n, b & n
            a = a ^ c
            a, b = a & (a ^ b), b & (a ^ b)   

        return b

'''
https://leetcode.com/problems/single-number-ii/discuss/43294/Challenge-me-thx
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once