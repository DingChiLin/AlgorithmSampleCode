from typing import List

class TrieNode:
    def __init__(self):
        self.child = {}
        self.go = 0  # Number of elements goes through this node
    def increase(self, number, d):
        cur = self
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child: cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            cur.go += d
    def findMax(self, number):
        cur, ans = self, 0
        for i in range(17, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child and cur.child[1-bit].go > 0:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            else:
                cur = cur.child[bit]
        return ans

class Solution:
    def maxGeneticDifference(self, parents: List[int], qs: List[List[int]]) -> List[int]:
        n, m, root = len(parents), len(qs), -1
        ans, trieNode = [-1] * m, TrieNode()
        graph, queryByNode = [[] for _ in range(n)], [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p == -1: root = i
            else: graph[p].append(i)

        for i, q in enumerate(qs):
            queryByNode[q[0]].append((q[1], i))  # node -> list of pairs (val, idx)

        def dfs(u):
            trieNode.increase(u, 1)
            for val, idx in queryByNode[u]:
                ans[idx] = trieNode.findMax(val)
            for v in graph[u]:
                dfs(v)
            trieNode.increase(u, -1)

        dfs(root)
        return ans