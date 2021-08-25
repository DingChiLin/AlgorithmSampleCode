from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        columnSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in columnSets[i]:
                        return False
                    else:
                        columnSets[i].add(board[i][j])
                        
                    if board[i][j] in rowSets[j]:
                        return False
                    else:
                        rowSets[j].add(board[i][j])
                                       
                    if board[i][j] in boxSets[i//3][j//3]:
                        return False
                    else:
                        boxSets[i//3][j//3].add(board[i][j])
        return True

s = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(board))