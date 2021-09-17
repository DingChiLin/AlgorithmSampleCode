from typing import List
from math import inf

class Solution:
    # 用 log(len(A) + len(B)) 的時間複雜度，在 A 與 B 的所有數中，找到第 k 大的數
    def findKth(self, A, B, k):
        '''
            leftX 代表的是要取多少 list X 內的元素
            目標是滿足以下兩條件：
                1. leftA + leftB == K (總共取 K 個元素)
                2. A[:leftA] + B[:leftB] 的內容物都小於 A[leftA:] + B[leftB:]
        '''
        leftA, rightA = 0, len(A)
        leftB, rightB = 0, len(B)
        while leftA < rightA and leftB < rightB:
            midA = (leftA + rightA) // 2
            midB = (leftB + rightB) // 2
            if midA + midB >= k:
                if A[midA] > B[midB]:
                    rightA = midA
                else:
                    rightB = midB
            else:
                if A[midA] > B[midB]:
                    leftB = midB + 1
                else:
                    leftA = midA + 1

        # 其中一邊的 list 已經被檢查完了，但另一邊還沒時，額外處理
        if leftA < rightA:
            leftA = k - leftB
        if leftB < rightB:
            leftB = k - leftA

        # 找到兩個 list 用到的最後一個數字，並取大的
        # 注意如果 leftX == 0 代表意義是使用了 0 個 X list 的元素，因此將值設負無限大
        numA = A[leftA - 1] if leftA > 0 else -inf
        numB = B[leftB - 1] if leftB > 0 else -inf
        return max(numA, numB)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1)
        M = len(nums2)
        if (N+M) % 2 == 0:
            return (self.findKth(nums1, nums2, (N+M)//2) + self.findKth(nums1, nums2, (N+M)//2 + 1)) / 2
        else:
            return self.findKth(nums1, nums2, (N+M)//2 + 1)

s = Solution()
A = [3]
B = [-2, -1]
print(s.findMedianSortedArrays(A, B))