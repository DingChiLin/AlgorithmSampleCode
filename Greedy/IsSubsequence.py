class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and c == s[i]:
                i += 1
            if i == len(s):
                break
        return i == len(s)


s = Solution()
str = "abx"
t = "ahbgdc"
print(s.isSubsequence(str, t))
