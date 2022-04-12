class SegmentTree:
    def __init__(self, A):
        self.N = len(A)
        self.seg_tree = [0] * 4 * self.N
        self.lazy = [0] * 4 * self.N
        self._build(A, 1, 0, self.N-1)

    def _build(self, A, v, tl, tr):
        if (tl == tr):
            self.seg_tree[v] = A[tl]
        else:
            tm = (tl + tr) // 2
            self._build(A, v*2, tl, tm)
            self._build(A, v*2+1, tm+1, tr)
            self.seg_tree[v] = self.seg_tree[v*2] + self.seg_tree[v*2+1]

    def push(self, v, tl, tr):
        self.seg_tree[v] += self.lazy[v] * (tr - tl + 1)
        if (tl < tr): # still have children
            self.lazy[v*2] += self.lazy[v]
            self.lazy[v*2+1] += self.lazy[v]
        
        self.lazy[v] = 0

    def _add(self, v, tl, tr, l, r, addend):
        self.push(v, tl, tr)
        if (l > r):
            return
        if (l == tl and tr == r):
            self.lazy[v] += addend
        else:
            tm = (tl + tr) // 2
            self._add(v*2, tl, tm, l, min(r, tm), addend)
            self._add(v*2+1, tm+1, tr, max(l, tm+1), r, addend)
            self.push(v*2, tl, tm)
            self.push(v*2+1, tm+1, tr)
            self.seg_tree[v] = self.seg_tree[v*2] + self.seg_tree[v*2+1]

    def add(self, l, r, addend):
        self._add(1, 0, self.N-1, l, r, addend)

    def _query(self, v, tl, tr, l, r):
        if (l > r):
            return 0
        self.push(v, tl, tr)
        if (l <= tl and tr <= r):
            return self.seg_tree[v]
        tm = (tl + tr) // 2
        return self._query(v*2, tl, tm, l, min(r, tm)) + self._query(v*2+1, tm+1, tr, max(l, tm+1), r)

    def query(self, l, r):
        return self._query(1, 0, self.N-1, l, r)

# for more info: https:#cp-algorithms.com/data_structures/segment_tree.html#toc-tgt-10

N = 17
nums = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5, 9, 2, 7]
tree = SegmentTree(nums)

print(tree.query(0, 16)) # 66
print(tree.query(0, 13)) # 48
print(tree.query(1, 1)) # 7
print(tree.query(6, 13)) # 24

tree.add(3, 3, 10); # 1, 7, 3, 10, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 76
print(tree.query(2, 3)) # 13
print(tree.query(0, 13)) # 58
print(tree.query(1, 1)) # 7
print(tree.query(6, 13)) # 24

tree.add(3, 10, 10); # 1, 7, 3, 20, 15, 18, 13, 12, 16, 12, 11, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 156
print(tree.query(2, 3)) # 23
print(tree.query(0, 13)) # 138
print(tree.query(1, 1)) # 7
print(tree.query(11, 13)) # 10

tree.add(0, 9, 1); # 2, 8, 4, 21, 16, 19, 14, 13, 17, 13, 11, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 166
print(tree.query(2, 3)) # 25
print(tree.query(0, 13)) # 148
print(tree.query(1, 1)) # 8
print(tree.query(11, 13)) # 10

tree.add(2, 4, -5); # 2, 8, -1, 16, 11, 19, 14, 13, 17, 13, 11, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 151
print(tree.query(2, 3)) # 15
print(tree.query(0, 13)) # 133
print(tree.query(1, 1)) # 8
print(tree.query(11, 13)) # 10

# total sum
print(tree.query(0, 16)) # 151