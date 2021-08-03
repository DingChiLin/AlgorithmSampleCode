from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        records = set()
        for n in nums:
            if n in records:
                return True
            records.add(n)
        return False