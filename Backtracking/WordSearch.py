from typing import List

# backtracking
class Solution:
    def __init__(self):
        self.ans = False
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def valid_position(self, r, c, n, m):
        return (0 <= r < n and 0 <= c < m)

    def backtracking(self, index, r, c, visited, word, board):
        if self.ans:
            return
        
        if (index == len(word)):
            self.ans = True
            return
        
        N = len(board)
        M = len(board[0])
        for (dx, dy) in self.moves:
            nr = r + dx
            nc = c + dy
            if not self.ans and \
                self.valid_position(nr, nc, N, M) and \
                board[nr][nc] == word[index] and \
                not visited[nr][nc]:

                visited[nr][nc] = True
                self.backtracking(index + 1, nr, nc, visited, word, board)
                visited[nr][nc] = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = False
        N = len(board)
        M = len(board[0])

        # Sanity check 1: too much words
        if len(word) > N*M:
            return False
        
        # Sanity check 2: exist a word which is not in board
        board_set = set([c for row in board for c in row]) # flatten the board into a set
        for w in set(word):
            if w not in board_set:
                return False

        # Backtracking
        visited = [[False for _ in range(M)] for _ in range(N)]
        for r in range(N):
            for c in range(M):
                if (board[r][c] == word[0]):
                    visited[r][c] = True
                    self.backtracking(1, r, c, visited, word, board)
                    visited[r][c] = False
        
        return self.ans

s = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(s.exist(board, word))