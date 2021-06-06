from typing import List

class Solution:
    def __init__(self):
        self.is_palindrome = None
        self.ans = None

    def find_palindrome(self, s):
        self.is_palindrome = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for j in range(len(s)):
            for i in range(0, j+1):
                if (s[i] == s[j]) and ( j - i < 2 or self.is_palindrome[i+1][j-1]):
                    self.is_palindrome[i][j] = True

    def helper(self, start, s, palindromes):
        if (start == len(s)):
            self.ans.append(palindromes[:])

        for i in range(start, len(s)):
            if (self.is_palindrome[start][i]):
                palindromes.append(s[start:i+1])
                self.helper(i+1, s, palindromes)
                palindromes.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.find_palindrome(s)
        self.ans = []
        self.helper(0, s, [])
        return self.ans

s = Solution()
input = "abaca"
print(s.partition(input))