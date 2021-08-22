from typing import List
from math import sqrt, sin, cos, acos, atan2

PI = acos(-1)
EPS = 1e-12

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, b):
        return Point(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        return Point(self.x - b.x, self.y - b.y)

    def mul(self, v):
        return Point(self.x * v, self.y * v)
    
    def div(self, v):
        return Point(self.x / v, self.y / v)

    def __mul__(self, b):
        return self.x * b.x + self.y * b.y # 內積

    def __xor__(self, b):
        return self.x * b.y - self.y * b.x # 外積
    
    def __lt__(self, b):
        return (self.x, self.y) < (b.x, b.y)

    # def __lt__(self, b): # 極角排序用
    #      return self.angle() < b.angle()
    
    def angle(self):
        return atan2(self.y, self.x)

    def includedAngle(self, b): # 夾角（保持正數）
        dot = self*b
        det = self^b
        ang = atan2(det, dot)
        if ang < 0:
            ang += 2 * PI
        return ang

    def dis(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def dis2(self, b):
        return sqrt((self.x - b.x) * (self.x - b.x) + (self.y - b.y) * (self.y - b.y))
    
    def rotate(self, v):
        return Point(self.x * cos(v) - self.y * sin(v), self.x * sin(v) + self.y * cos(v))

    def rotate90(self):
         return Point(-self.y, self.x)

    def unit(self):
        return self.div(self.dis())

    def __repr__(self):
        return str((self.x, self.y))

# Convex Hull
class Solution:
    def convexHull(self, points):
        N = len(points)
        points.sort()
        stk = []

        for i in range(N):
            # 若要排除邊上得點，後面改 <=
            while(len(stk) > 1 and ((points[stk[-1]] - points[stk[-2]]) ^ (points[i] - points[stk[-1]])) < 0):
                stk.pop()
            stk.append(i)
    
        tmp = len(stk)
        for i in range(N-2, -1, -1):
            # 若要排除邊上得點，後面改 <=
            while(len(stk) > tmp and ((points[stk[-1]] - points[stk[-2]]) ^ (points[i] - points[stk[-1]])) < 0):
                stk.pop()
            stk.append(i)

        return [points[i] for i in set(stk)]

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = [Point(x, y) for x, y in trees]
        convexHulls = self.convexHull(points)
        return [[p.x, p.y] for p in convexHulls]

s = Solution()
points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
points = [[1,2],[2,2],[4,2]]
points = [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[3,3]]
print(s.outerTrees(points))