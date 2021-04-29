class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stk = []
        for i in range(len(nums2)):
            while(len(stk) and nums2[i] > nums2[stk[-1]]):
                mapping[nums2[stk[-1]]] = nums2[i]
                stk.pop()
            stk.append(i)
            
        ans = []
        for n in nums1:
            if (n in mapping):
                ans.append(mapping[n])
            else:
                ans.append(-1)
        return ans
