class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        
        # Count of '(', ')' and free positions
        L, R, F = 0, 0, 0
        for i in range(N):
            if locked[i] == '0':
                F += 1
            else:
                if s[i] == '(':
                    L += 1
                else:
                    R += 1
        FL2 = (F + R - L)
        if (FL2 & 1) or (FL2 < 0): 
            # It's impossible make the total count of '(' and ')' balanced by using free positions
            return False

        # how many free position should become '(', the others will become ')'
        FL = FL2 // 2

        # Greedy: if we can choose some free position to be '(', the sooner the better
        stk = 0
        for i in range(N):
            if locked[i] == '0':
                if FL > 0:
                    stk += 1
                    FL -= 1
                else:
                    stk -= 1
            else:
                if s[i] == '(':
                    stk += 1
                else:
                    stk -= 1
            if stk < 0:
                return False
        return stk == 0
                
            
        