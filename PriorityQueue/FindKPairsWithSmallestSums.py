from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
            
        pq = [(nums1[0] + nums1[0], (0,0))]
        count = 0
        visited = set([(0,0)])
        result = []
        while pq:
            if count == k:
                break

            _, indexes = heapq.heappop(pq)
            result.append(list(indexes))
            i1, i2 = indexes
            if i1 < len(nums1) - 1:
                if (i1 + 1, i2) not in visited:
                    heapq.heappush(pq, (nums1[i1 + 1] + nums2[i2], (i1 + 1, i2)))
                    visited.add((i1 + 1, i2))

            if i2 < len(nums2) - 1:
                if (i1, i2 + 1) not in visited:
                    heapq.heappush(pq, (nums1[i1] + nums2[i2 + 1], (i1, i2 + 1)))
                    visited.add((i1, i2 + 1))

            count += 1

        return [[nums1[i[0]], nums2[i[1]]] for i in result]


s = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3


nums1 = [1,2]
nums2 = [3]
k = 3
print(s.kSmallestPairs(nums1, nums2, k))