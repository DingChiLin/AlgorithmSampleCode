from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        records = set()
        for n in nums:
            if n in records:
                return False
            records.add(n)
        return True