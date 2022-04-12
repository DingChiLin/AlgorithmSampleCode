from math import inf

class SegmentTree:
    def __init__(self, A):
        self.N = len(A)
        self.seg_tree = [0] * 4 * self.N
        self.lazy = [-inf] * 4 * self.N
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
        if (self.lazy[v] > -inf):
            self.seg_tree[v] = self.lazy[v] * (tr - tl + 1)
            if (tl < tr): # still have children
                self.lazy[v*2] = self.lazy[v]
                self.lazy[v*2+1] = self.lazy[v]
            self.lazy[v] = -inf

    def _update(self, v, tl, tr, l, r, addend):
        self.push(v, tl, tr)
        if (l > r):
            return
        if (l == tl and tr == r):
            self.lazy[v] = addend
        else:
            tm = (tl + tr) // 2
            self._update(v*2, tl, tm, l, min(r, tm), addend)
            self._update(v*2+1, tm+1, tr, max(l, tm+1), r, addend)
            self.push(v*2, tl, tm)
            self.push(v*2+1, tm+1, tr)
            self.seg_tree[v] = self.seg_tree[v*2] + self.seg_tree[v*2+1]

    def update(self, l, r, addend):
        self._update(1, 0, self.N-1, l, r, addend)

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


nums = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5, 9, 2, 7]
tree = SegmentTree(nums)

print("===1===")
print(tree.query(0, 16)) # 66
print(tree.query(0, 13)) # 48
print(tree.query(1, 1)) # 7
print(tree.query(6, 13)) # 24

print("===2===")
tree.update(3, 3, 10); # 1, 7, 3, 10, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 76
print(tree.query(2, 3)) # 13
print(tree.query(0, 13)) # 58
print(tree.query(1, 1)) # 7
print(tree.query(6, 13)) # 24

print("===3===")
tree.update(3, 10, 10); # 1, 7, 3, 10, 10, 10, 10, 10, 10, 10, 10, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 119
print(tree.query(2, 3)) # 13
print(tree.query(0, 13)) # 101
print(tree.query(1, 1)) # 7
print(tree.query(11, 13)) # 10

print("===4===")
tree.update(0, 9, 1); # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 48
print(tree.query(2, 3)) # 2
print(tree.query(0, 13)) # 30
print(tree.query(1, 1)) # 1
print(tree.query(11, 13)) # 10

print("===5===")
tree.update(2, 4, -5); # 1, 1, -5, -5, -5, 1, 1, 1, 1, 1, 10, 1, 4, 5, 9, 2, 7
print(tree.query(0, 16)) # 30
print(tree.query(2, 3)) # -10
print(tree.query(0, 13)) # 12
print(tree.query(1, 1)) # 1
print(tree.query(11, 13)) # 10
