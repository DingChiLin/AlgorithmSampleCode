from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])
        
        # bisect right on first column
        left = 0
        right = N
        while(left < right):
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid
            else:
                left = mid + 1

        row = left - 1 # find row

        if row == -1:
            return False
        if matrix[row][0] == target:
            return True

        # bisect left on row
        left = 0
        right = M
        while(left < right):
            mid = (left + right) // 2
            if matrix[row][mid] >= target:
                right = mid
            else:
                left = mid + 1

        if left < M and matrix[row][left] == target:
            return True
        else:
            return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13
print(s.searchMatrix(matrix, target))