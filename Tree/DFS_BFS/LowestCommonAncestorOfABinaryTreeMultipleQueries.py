from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:

    def get_time(self, node, edges, in_time, out_time):
        self.timer += 1
        in_time[node] = self.timer
        for child in edges[node]:
            self.get_time(child, edges, in_time, out_time)
        self.timer += 1
        out_time[node] = self.timer

    # is p an ancestor of q
    def is_ancestor(self, p, q, in_time, out_time):
        return in_time[p] < in_time[q] and out_time[p] > out_time[q]

    def lowestCommonAncestor(self, parents, queries):
        N = len(parents)

        root = 0
        edges = defaultdict(list)
        for n, p in enumerate(parents):
            if p == -1:
                root = n
            edges[p].append(n)

        in_time = [0 for _ in range(N)]
        out_time = [0 for _ in range(N)]
        self.timer = 0
        self.get_time(root, edges, in_time, out_time)

        ancestor = [[0 for _ in range(N)] for i in range(N.bit_length()+1)]
        ancestor[0] = parents

        for i in range(1, N.bit_length()+1):
            for j in range(N):
                if ancestor[i-1][j] == -1:
                    ancestor[i][j] = -1
                else:
                    ancestor[i][j] = ancestor[i-1][ancestor[i-1][j]]

        ans = []
        for p, q in queries:
            if self.is_ancestor(p, q, in_time, out_time):
                ans.append(p)
            elif self.is_ancestor(q, p, in_time, out_time):
                ans.append(q)
            else:
                for i in range(N.bit_length(), -1, -1):
                    anc = ancestor[i][p]
                    if anc == -1:
                        continue
                    if self.is_ancestor(anc, q, in_time, out_time):
                        continue
                    else:
                        p = anc
                ans.append(ancestor[0][p])

        return ans




'''
Tree:
     4
   2   6
  1 3 5 7 
   8 9   0
'''

N = 10
parents = [7,2,4,2,-1,6,4,6,3,3]
queries = [[2,6], [4,6], [7,6], [8,9], [9,1], [8,7], [0,1], [5,7]]

S = Solution()
print(S.lowestCommonAncestor(parents, queries)) # 4, 4, 6, 3, 2, 4, 4, 6
