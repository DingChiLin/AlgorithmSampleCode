from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        stk = []
        visited = set()
        for c in s:
            if c in visited:
                counter[c] -= 1
                continue
            while len(stk) and c < stk[-1] and counter[stk[-1]] >= 1:
                visited.remove(stk[-1])
                stk.pop()
            stk.append(c)
            visited.add(c)
            counter[c] -= 1
        return "".join(stk)
