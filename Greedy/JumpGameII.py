from typing import List

# forward
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        max_possible = 0
        current_end = 0
        ans = 0
        for i in range(N-1):
            max_possible = max(i + nums[i], max_possible)
            if i == current_end:
                ans += 1
                current_end = max_possible
        return ans

# reverse + stack
class Solution2:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        stk = [(N-1, 0)] # [position, need_step]
        for i in range(N - 2, -1, -1):
            while len(stk) > 1 and (i + nums[i]) >= stk[-2][0]:
                stk.pop()
            
            stk.append((i, stk[-1][1] + 1))
        return stk[-1][1]

s = Solution()
nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
print(s.jump(nums))