from typing import List
from collections import deque

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        N = len(boxes)
        DP = [0 for _ in range(N+1)]
        que = deque()
        curWeight = 0
        curBoxes = 0
        i = 0
        for j in range(N):
            p, w = boxes[j]
            while que and i < j and (curWeight + w > maxWeight or curBoxes + 1 > maxBoxes or DP[i+1] == DP[i]):
                rp, rw = boxes[i]
                que[0][1] -= 1
                if que[0][1] == 0:
                    que.popleft()
                curWeight -= rw
                curBoxes -= 1
                i += 1

            curWeight += w
            curBoxes += 1
            if que and que[-1][0] == p:
                que[-1][1] += 1
            else:
                que.append([p, 1])

            curCost = 2 + len(que) - 1 + DP[i]
            DP[j+1] = curCost
        return DP[N]


s = Solution()

# boxes = [[1,1],[2,1],[1,1]]
# portsCount = 2
# maxBoxes = 3
# maxWeight = 3
# print(s.boxDelivering(boxes, portsCount, maxBoxes, maxWeight)) # 4

# boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]]
# portsCount = 3
# maxBoxes = 3
# maxWeight = 6
# print(s.boxDelivering(boxes, portsCount, maxBoxes, maxWeight)) # 6

boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]]
portsCount = 3
maxBoxes = 6
maxWeight = 7
print(s.boxDelivering(boxes, portsCount, maxBoxes, maxWeight)) # 6

boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]]
portsCount = 5
maxBoxes = 5
maxWeight = 7
print(s.boxDelivering(boxes, portsCount, maxBoxes, maxWeight)) # 14

