from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for n in asteroids:
            explode = False
            if n < 0:
                while stk and stk[-1] >= 0:
                    if abs(n) > stk[-1]:
                        stk.pop()
                    elif abs(n) < stk[-1]:
                        explode = True
                        break
                    else:
                        stk.pop()
                        explode = True
                        break

            if not explode:
                stk.append(n)

        return stk

s = Solution()
asteroids = [-2,-1,1,2]
print(s.asteroidCollision(asteroids))