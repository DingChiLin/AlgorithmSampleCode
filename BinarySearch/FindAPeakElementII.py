from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        leftRow = 0
        rightRow = len(mat) - 1

        while (leftRow <= rightRow):
            midRow = (leftRow + rightRow) // 2

            maxValue = 0
            maxCol = 0
            for col in range(len(mat[midRow])):
                if mat[midRow][col] > maxValue:
                    maxValue = mat[midRow][col]
                    maxCol = col
            
            if midRow > 0 and mat[midRow - 1][maxCol] > mat[midRow][maxCol]:
                rightRow = midRow - 1
            elif midRow < len(mat) - 1 and mat[midRow + 1][maxCol] > mat[midRow][maxCol]:
                leftRow = midRow + 1
            else:
                return [midRow, maxCol]