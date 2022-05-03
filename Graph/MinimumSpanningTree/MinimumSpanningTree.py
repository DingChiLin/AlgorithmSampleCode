import heapq

# Prim
class MST:
    def find(self, nodes, edges):
        s = nodes[0]
        N = len(nodes)

        pq = []
        for v, w in edges[s]:
            heapq.heappush(pq, (w, s, v)) # (weight, u, v)
        visited = set([s])

        tree = []
        weight = 0
        while len(visited) < N:
            w, u, v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            tree.append([u, v])
            weight += w
            for nv, nw in edges[v]:
                if nv not in visited:
                    heapq.heappush(pq, (nw, v, nv))

        return weight, tree

class UnionFind:
    def __init__(self, N):
        self.nodes = [i for i in range(N)]
        self.rank = [1 for i in range(N)]       

    def root(self, n):
        if n != self.nodes[n]:
            self.nodes[n] = self.root(self.nodes[n])
        return self.nodes[n]

    def union(self, n1, n2):
        r1 = self.root(n1)
        r2 = self.root(n2)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.nodes[r1] = r2
            elif self.rank[r1] > self.rank[r2]:
                self.nodes[r2] = r1
            else:
                self.nodes[r2] = r1
                self.rank[r1] += 1
            return True
        return False

# Kruskal
class MST2:
    def find(self, nodes, edges):
        UF = UnionFind(max(nodes) + 1) # create enough space for union find array
        sorted_edges = sorted([(w, u, v) for u, edge in edges.items() for v, w in edge])
        mst = []
        weight = 0
        for w, u, v in sorted_edges:
            if UF.union(u, v):
                mst.append([u, v])
                weight += w
        return weight, mst

#        5    7
#     1 -- 3 -- 5
#   1/   2/ 1\ /3 
#  0 -- 2 -- 4
#     3    8

nodes = list(range(6))
edges = {
    0: [[1, 1], [2, 3]],
    1: [[0, 1], [3, 5]],
    2: [[0, 3], [3, 2], [4, 8]],
    3: [[1, 5], [2, 2], [4, 1], [5, 7]],
    4: [[2, 8], [3, 1], [5, 3]],
    5: [[3, 7], [4, 3]]
}

mst = MST()
mst2 = MST2()
print(mst.find(nodes, edges))
print(mst2.find(nodes, edges))
