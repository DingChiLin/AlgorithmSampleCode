from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        visited = set()
        que = deque([("0000", 0)])
        while que:
            n, d = que.popleft()
            if n == target:
                return d
            for i in range(4):
                # add 1 
                nxt1 = n[:i] + str((int(n[i]) + 1) % 10) + n[i+1:]
                if nxt1 not in visited and nxt1 not in deadends:
                    visited.add(nxt1)
                    que.append((nxt1, d + 1))

                # add 9 (MOD 10) = minus 1
                nxt2 = n[:i] + str((int(n[i]) + 9) % 10) + n[i+1:]
                if nxt2 not in visited and nxt2 not in deadends:
                    visited.add((nxt2))
                    que.append((nxt2, d + 1))

        return -1


s = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(s.openLock(deadends, target))