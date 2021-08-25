from typing import List
from math import ceil

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = ceil(c ** 0.5)
        while i <= j:
            n = i * i + j * j
            if n == c:
                return True
            elif n > c:
                j -= 1
            else:
                i += 1
        return False