from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dst = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
        for n1, n2, d in edges:
            dst[n1][n2] = d
            dst[n2][n1] = d

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])
 
        min_cnt = float('inf')
        min_node = None
        for i, ds in enumerate(dst):
            cnt = len([d for d in ds if d <= distanceThreshold])
            if cnt <= min_cnt:
                min_cnt = cnt
                min_node = i
        return min_node