from typing import List

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        ans = ""
        for c in s:
            if c == '(':
                if cnt != 0:
                    ans += c
                cnt += 1
            else:
                cnt -= 1
                if cnt != 0:
                    ans += c
        return ans

s = Solution()
ss = "(()())(())(()(()))"
print(s.removeOuterParentheses(ss))