from math import sqrt, sin, cos, acos, atan2, pi

PI = pi
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

    def angle360(self):
        return (atan2(self.y, self.x) * 180 / PI) % 360

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

def intersection(a, b, c, d):

    # 共線
    if (max(a.x, b.x) < min(c.x, d.x)):
        return False

    if (max(c.x, d.x) < min(a.x, b.x)):
        return False

    if (max(a.y, b.y) < min(c.y, d.y)):
        return False

    if (max(c.y, d.y) < min(a.y, b.y)):
        return False

    # 交錯(有一點碰到就算數)
    area1 = (b-a) * (c-a)
    area2 = (b-a) * (d-a)
    if (area1 * area2 > 0): # 等於代表點在線上
        return False

    area3 = (c-d) * (a-d)
    area4 = (c-d) * (b-d)
    if (area3 * area4 > 0): # 等於代表點在線上
        return False

    return True

# ab intersect cd (延伸線也適用)
def intersectionPoint(a, b, c, d):
    ACD = ((a-c)*(a-d)) # can't take abs value
    BCD = ((b-d)*(b-c))
    return (a * BCD + b * ACD) / (ACD + BCD)

# 外心
def circumcentre(a, b, c):
    m1 = (a+b)/2
    m2 = (a+c)/2
    normalAB = (a-b).rotate90()
    normalAC = (a-c).rotate90()
    o = intersectionPoint(m1, m1 + normalAB, m2, m2 + normalAC)
    return o

def main():
    p1 = Point(3, 4)
    print(p1)
    p2 = Point(4, 3)
    print(p1.angle())

    p3 = Point(1, 9)
    points = [p1, p2, p3]
    points.sort()
    print(points)

main()