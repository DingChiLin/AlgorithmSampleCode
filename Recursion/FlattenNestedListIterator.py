# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from re import A
from typing import List
class NestedInteger:
    def __init__(self, val = None, lst = None):
        self.val = val
        self.lst = lst

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.val != None

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.val if self.val != None else None


    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.lst if self.lst != None else None

class NestedIterator:
    def __init__(self, nestedList):
        self.stk = [nestedList]
        self.idx = [0]

    def next(self) -> int:
        self.hasNext()
        stk = self.stk[-1]
        idx = self.idx[-1]
        n = stk[idx].getInteger()
        self.idx[-1] += 1
        return n

    def hasNext(self) -> bool:
        while self.stk:
            stk = self.stk[-1]
            idx = self.idx[-1]
            if idx == len(stk):
                self.stk.pop()
                self.idx.pop()
            else:
                x = stk[idx]
                if x.isInteger():
                    return True
                self.idx[-1] += 1
                self.stk.append(x.getList())
                self.idx.append(0)
        return False

n1 = NestedInteger(1, None)
n2 = NestedInteger(2, None)
n3 = NestedInteger(3, None)
n4 = NestedInteger(4, None)
n5 = NestedInteger(5, None)
n6 = NestedInteger(6, None)
n7 = NestedInteger(7, None)
l1 = NestedInteger(None, [n1, n2])
l2 = NestedInteger(None, [n4, n5, n6])
l3 = NestedInteger(None, [l1, l2])
nn = NestedInteger(None, [])

i, v = NestedIterator([l1, n3, l2, nn, n7, l3]), []
# i, v = NestedIterator([nn]), []

while i.hasNext():
     v.append(i.next())
print(v)