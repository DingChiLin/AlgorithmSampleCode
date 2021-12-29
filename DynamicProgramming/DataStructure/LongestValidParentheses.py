class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        DP = [0] * (N+1)
        stk = []
        ans = 0
        for i in range(1, N+1):
            c = s[i-1]
            if c == '(':
                stk.append(i)
            else:
                if stk:
                    last = stk.pop()
                    DP[i] = DP[last - 1] + (i-last+1)
                    ans = max(ans, DP[i])
        return ans
                