# [Leetcode 47](https://leetcode.com/problems/permutations-ii/)

from typing import List, Set

class Solution:
    def __init__(self):
        self.ans = []

    # Note: we use `id` instead of `value` in the used set.
    def find(self, used: Set[int], nums: List[int], permutation: List[int]):
        if (len(used) == len(nums)):
            self.ans.append(permutation[:])
            return

        seen = set() # prevent using same number in the same level
        for i, n in enumerate(nums):
            if (i in used) or (n in seen):
                continue
            seen.add(n)

            used.add(i)
            permutation.append(n)
            self.find(used, nums, permutation)
            used.remove(i)
            permutation.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.find(set(), nums, [])
        return self.ans

s = Solution()
nums = [1,1,2]
print(s.permuteUnique(nums))
