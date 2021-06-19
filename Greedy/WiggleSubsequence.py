from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 0
        stk = []
        for i in range(len(nums)):
            n = nums[i]
            if len(stk) == 0 or \
               len(stk) == 1 and n != stk[-1]:
                stk.append(n)
                ans += 1
                continue

            if n == stk[-1]:
                continue
            elif (n - stk[-1]) * (stk[-1] - stk[-2]) > 0:
                stk.pop()
                stk.append(n)
            else:
                stk.append(n)
                ans += 1

        return ans

s = Solution()
nums = [1,7,4,9,2,5]
print(s.wiggleMaxLength(nums))