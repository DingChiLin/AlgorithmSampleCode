from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        i = 0
        records = {}
        maxCount = 0
        for j in range(N):
            if s[j] not in records:
                records[s[j]] = True
                maxCount = max(maxCount, len(records))
            else:
                while s[i] != s[j]:
                    del records[s[i]]
                    i += 1 
                i += 1
        return maxCount
                