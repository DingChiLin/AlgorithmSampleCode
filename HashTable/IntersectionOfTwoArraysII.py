from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for n in nums1:
            hash1[n] += 1
        for n in nums2:
            hash2[n] += 1
        
        merged = {}
        for key, val in hash1.items():
            if key in hash2:
                merged[key] = min(val, hash2[key])

        ans = []
        for key, val in merged.items():
            for _ in range(val):
                ans.append(key)

        return ans