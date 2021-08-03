from typing import List

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for c in s:
            if c == '(':
                stk.append(c)
            else:
                score = 0
                while stk:
                    if stk[-1] == '(':
                        if score == 0:
                            score = 1
                        else:
                            score *= 2
                        stk.pop()
                        break
                    else:
                        score += stk[-1]
                        stk.pop()
                stk.append(score)
        return sum(stk)

s = Solution()
ss = "(()(()))"
ss = "()()"
print(s.scoreOfParentheses(ss))