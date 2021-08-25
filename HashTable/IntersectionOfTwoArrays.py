from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        records = set(nums2)
        ans = []
        for n in set(nums1):
            if n in records:
                ans.append(n)
        return ans