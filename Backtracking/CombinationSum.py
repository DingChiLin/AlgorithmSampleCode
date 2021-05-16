# [Leetcode 39](https://leetcode.com/problems/combination-sum/)

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(index, total, comb):
            if total == target:
                ans.append(comb[:])
                return

            if total > target:
                return

            if (index >= len(candidates)):
                return

            # use this index
            comb.append(candidates[index])
            helper(index, total + candidates[index], comb)
            comb.pop()

            # not use this index
            helper(index + 1, total, comb)

        helper(0, 0, [])
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # candidates.sort()
        def helper(start_index, total, comb):
            if total == target:
                ans.append(comb[:])
                return

            if total > target:
                return

            for i in range(start_index, len(candidates)):
                # if (total + candidates[i] > target):
                #     break
                comb.append(candidates[i])
                helper(i, total + candidates[i], comb)
                comb.pop()

        helper(0, 0, [])
        return ans

s = Solution()
candidates = [3,2,5]
target = 8
print(s.combinationSum(candidates, target))
print(s.combinationSum2(candidates, target))