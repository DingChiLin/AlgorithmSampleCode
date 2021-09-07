from typing import List
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = []
        N = len(mat)
        M = len(mat[0])
        value = sum([mat[i][0] for i in range(N)])
        indexes = [0 for i in range(N)]
        heapq.heappush(heap, (value, indexes[:]))
        seen = set()
        for _ in range(k-1):
            value, indexes = heapq.heappop(heap)
            for i in range(N):
                if indexes[i] + 1 < M:
                    indexes[i] += 1
                    if tuple(indexes) not in seen:
                        new_value = value + mat[i][indexes[i]] - mat[i][indexes[i] - 1]
                        heapq.heappush(heap, (new_value, indexes[:]))
                        seen.add(tuple(indexes))
                    indexes[i] -= 1
        return heap[0][0]

s = Solution()
mat = [[1,10,10],[1,4,5],[2,3,6]]
k = 7

print(s.kthSmallest(mat, k))