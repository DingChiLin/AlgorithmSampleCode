class Solution:
    # O(N^2)
    def reverse(self, str):
        if len(str) == 0:
            return ""
        else:
            return str[-1] + self.reverse(str[:-1]) # str[:-1] is an O(N) operation

    # O(N)
    def reverse2(self, str):
        def helper(end):
            if end == -1:
                return ""
            else:
                return str[end] + helper(end - 1)
        return helper(len(str) - 1)

s = Solution()
str = "abcde"
print(s.reverse(str))
print(s.reverse2(str))