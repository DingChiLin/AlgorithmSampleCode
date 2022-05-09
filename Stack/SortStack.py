class Solution:
    def sort(self, stk):
        helper_stk = []
        while stk:
            n = stk.pop()
            while helper_stk and helper_stk[-1] > n:
                m = helper_stk.pop()
                stk.append(m)
            helper_stk.append(n)

        while helper_stk:
            stk.append(helper_stk.pop())
        return stk

S = Solution()
stk = [1,5,7,4,2,3,9,8,6]
print(S.sort(stk))
