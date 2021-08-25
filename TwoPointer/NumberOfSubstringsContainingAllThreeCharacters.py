from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        ans = 0
        records = defaultdict(int)
        for j in range(len(s)):
            records[s[j]] += 1
            while i < len(s) and len(records) == 3:
                records[s[i]] -= 1
                if records[s[i]] == 0:
                    del records[s[i]]
                i += 1
            ans += i

        return ans

s = Solution()
ss = "abcabc"
print(s.numberOfSubstrings(ss))