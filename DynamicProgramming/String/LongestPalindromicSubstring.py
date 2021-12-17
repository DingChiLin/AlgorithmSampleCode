class Solution:
    def __init__(self):
        self.maxLength = 0
        self.ans = (0, 0)
    
    def extend(self, s, i, j):
        maxLength = 0
        interval = (0, 0)
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                length = (j - i + 1)
                if length > maxLength:
                    maxLength = length
                    interval = (i, j)
            else:
                break
            i-=1
            j+=1
        return (maxLength, interval[0], interval[1])
            
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        maxLength = 0
        interval = ()
        # odd
        for i in range(N):
            length, left, right = self.extend(s, i, i)
            if length > maxLength:
                maxLength = length
                interval = (left, right)

        # even
        for i in range(1, N):
            length, left, right = self.extend(s, i-1, i)
            if length > maxLength:
                maxLength = length
                interval = (left, right)
        
        return s[interval[0]: interval[1]+1]