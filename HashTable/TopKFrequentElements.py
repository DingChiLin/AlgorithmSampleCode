from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1 
        sortedCounter = sorted([(count, num) for num, count in counter.items()], reverse = True)
        return [num for count, num in sortedCounter[:k]]



