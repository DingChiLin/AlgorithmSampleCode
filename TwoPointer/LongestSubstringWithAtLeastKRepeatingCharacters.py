from collections import defaultdict

class Solution:
    def valid(self, counter, k):
        return all([n >= k for n in counter.values()])
    
    def longestSubstringWithMUniqCharacters(self, s, k, m):
        N = len(s)
        counter = defaultdict(int)
        i = 0
        ans = 0
        for j in range(N):
            counter[s[j]] += 1
            while i < N and len(counter) > m:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            if len(counter) == m and self.valid(counter, k):
                ans = max(ans, j - i + 1)
        return ans

    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for m in range(1, 27):
            ans = max(ans, self.longestSubstringWithMUniqCharacters(s, k, m))

        return ans


s = Solution()
ss = "ababbc"
k = 2
print(s.longestSubstring(ss, k))