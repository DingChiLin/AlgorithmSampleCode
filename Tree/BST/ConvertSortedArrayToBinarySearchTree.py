from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])

        middle = (start + end) // 2
        node = TreeNode(nums[middle])
        node.left = self.build(nums, start, middle-1)
        node.right = self.build(nums, middle+1, end)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums)-1)

s = Solution()
nums = [-10,-3,0,5,9]
s.sortedArrayToBST(nums)