from typing import List

class Solution:
    def __init__(self):
        self.ans = None

    def backtracking(self, col_set, add_set, substract_set, records, row, n):
        if row == n:
            tmp = [['.' for _ in range(n)]  for _ in range(n)]
            for r, c in records:
                tmp[r][c] = 'Q'
            self.ans.append([''.join(r) for r in tmp])

        for col in range(n):
            if not (col in col_set or row - col in substract_set or row + col in add_set):
                records.append((row, col))
                col_set.add(col)
                add_set.add(row + col)
                substract_set.add(row - col)
                self.backtracking(col_set, add_set, substract_set, records, row + 1, n)
                records.pop()
                col_set.remove(col)
                add_set.remove(row + col)
                substract_set.remove(row - col)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []                      
        self.backtracking(set(), set(), set(), [], 0, n)
        return self.ans

s = Solution()
n = 4
print(s.solveNQueens(n))