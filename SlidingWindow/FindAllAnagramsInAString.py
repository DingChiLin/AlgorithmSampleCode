from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        target = Counter(p)
        cur = Counter()
        i = 0
        N = len(s)
        k = len(p)
        for j in range(N):
            cur[s[j]] += 1
            if j - i == k: 
                cur[s[i]] -= 1
                if cur[s[i]] == 0: # need to delete key when count == 0
                    del cur[s[i]]
                i += 1
            if cur == target:
                ans.append(i)
        return ans

s = Solution()
ss = "cbaebabacd"
p = "abc"

# ss = "abbaa"
# p = "aba"
print(s.findAnagrams(ss, p))