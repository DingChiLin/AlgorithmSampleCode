from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        ans = 0
        for i in range(len(boxTypes)):
            size, unit = boxTypes[i]
            if truckSize >= size:
                truckSize -= size
                ans += unit * size
            else:
                ans += unit * truckSize
                break
        return ans

s = Solution()
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(s.maximumUnits(boxTypes, truckSize))