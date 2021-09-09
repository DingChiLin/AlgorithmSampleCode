class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        stk = []
        for i in range(N):
            if s[i] == ']':
                strings = []
                nums = []

                # string part
                while stk and stk[-1] != '[':
                    c = stk.pop()
                    strings.append(c)

                # pop the [ character 
                stk.pop() 
                
                # number part
                while stk and stk[-1].isdigit():
                    n = stk.pop()
                    nums.append(n)
                
                stk.append(''.join(strings[::-1]) * int(''.join(nums[::-1])))
            else:
                stk.append(s[i])
        return ''.join(stk)