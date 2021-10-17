class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        stk = []
        N = len(s)
        cnt = len([c for c in s if c == letter])
        need = repetition
        for i, c in enumerate(s):
            while stk and c < stk[-1] and len(stk) + (N-i) > k and (stk[-1] != letter or cnt > need):
                n = stk.pop()
                if n == letter:
                    need += 1

            if len(stk) < k:
                if c == letter:
                    stk.append(c)
                    need -= 1   
                else:
                    if k - len(stk) > need:
                        stk.append(c)

            if c == letter:
                cnt -= 1

        return ''.join(stk)