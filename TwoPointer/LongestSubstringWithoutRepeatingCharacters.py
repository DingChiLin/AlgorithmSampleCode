from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        i = 0
        records = set()
        maxCount = 0
        for j in range(N):
            while s[j] in records:
                records.remove(s[i])
                i += 1
            records.add(s[j])
            maxCount = max(maxCount, j - i + 1)
        return maxCount
                