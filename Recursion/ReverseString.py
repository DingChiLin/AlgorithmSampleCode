class Solution:
    # O(N^2)
    def reverse(self, str):
        if len(str) == 0:
            return ""
        else:
            return str[-1] + self.reverse(str[:-1]) # str[:-1] is an O(N) operation

s = Solution()
str = "abcde"
print(s.reverse(str))
