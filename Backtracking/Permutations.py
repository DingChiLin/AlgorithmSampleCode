# [Leetcode 46](https://leetcode.com/problems/permutations/)

from typing import List, Set

# Use `visited` set to record number which has been visited before.
class Solution:
    def __init__(self):
        self.ans = []

    def find(self, visited: Set[int], nums: List[int], permutation: List[int]):
        if (len(visited) == len(nums)):
            self.ans.append(permutation[:])
            return

        for n in nums:
            if n not in visited:
                visited.add(n)
                permutation.append(n)
                self.find(visited, nums, permutation)
                visited.remove(n)
                permutation.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.find(set(), nums, [])
        return self.ans

# Remove value from set after visiting. 
class Solution2:
    def __init__(self):
        self.ans = []

    def find(self, nums_set: Set[int], permutation: List[int]):
        if (len(nums_set) == 0):
            self.ans.append(permutation[:])
            return

        for n in list(nums_set):
            nums_set.remove(n)
            permutation.append(n)
            self.find(nums_set, permutation)
            nums_set.add(n)
            permutation.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.find(set(nums), [])
        return self.ans

s = Solution()
nums = [1,2,3]
print(s.permute(nums))
