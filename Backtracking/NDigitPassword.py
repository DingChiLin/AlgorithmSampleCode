from typing import List

class Solution:
    def create(self, depth: int, max_depth: int, password: List[int]):
        if (depth == max_depth):
            print(password)
            return

        for i in range(3):
            password.append(i + 1)
            self.create(depth + 1, max_depth, password)
            password.pop()

    def find_all_passwords(self: int, digits: List[int]):
        self.create(0, digits, [])

s = Solution()
N = 3
s.find_all_passwords(N)
