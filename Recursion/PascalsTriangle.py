from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, n, rows):
        self.ans.append(rows)
        if n == 1:
            return
        nextRows = []
        nextRows.append(1)
        for i in range(1, len(rows)):
            nextRows.append(rows[i] + rows[i-1])
        nextRows.append(1)
        self.dfs(n-1, nextRows)

    def generate(self, numRows: int) -> List[List[int]]:
        self.dfs(numRows, [1])
        return self.ans

s = Solution()
numRows = 5
print(s.generate(numRows))