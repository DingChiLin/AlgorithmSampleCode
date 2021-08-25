class UnionFind:
    def __init__(self, N):
        self.father = [i for i in range(N)]
        self.rank = [1 for i in range(N)]       

    def root(self, n):
        if n != self.father[n]:
            self.father[n] = self.root(self.father[n])
        return self.father[n]

    def union(self, n1, n2):
        r1 = self.root(n1)
        r2 = self.root(n2)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.father[r1] = r2
            elif self.rank[r1] > self.rank[r2]:
                self.father[r2] = r1
            else:
                self.father[r2] = r1
                self.rank[r1] += 1
            return True
        return False

N, edges = 9, [[0, 3], [1, 6], [3, 7], [4, 4], [6, 1], [7, 8], [2, 5], [5, 2], [8, 0]]
u = UnionFind(N)
for (n1, n2) in edges:
    u.union(n1, n2)

#[0, 1, 2, 0, 4, 2, 1, 0, 0]
for i in range(N):
    print(u.root(i))