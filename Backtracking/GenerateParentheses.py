from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper("", n, n)

    def helper(self, curStr, left , right):
        if left == 0:
            for i in range(right):
                curStr += (')')
            return [curStr]
        elif left == right:
            return self.helper(curStr + '(', left-1, right)
        else:
            return \
                self.helper(curStr + '(', left-1, right) + \
                self.helper(curStr + ')', left, right-1)