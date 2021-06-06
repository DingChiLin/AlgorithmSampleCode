# [CSES Tower of Hanoi](https://cses.fi/problemset/task/2165)

class Solution:
    def count_step(self, n):
        if (n == 0):
            return 0
        else:
            return 2 * self.count_step(n-1) + 1

    def print_step_detail(self, start, buffer, end, n):
        if (n == 1):
            print(start, end)
        else:
            self.print_step_detail(start, end, buffer, n-1)
            self.print_step_detail(start, buffer, end, 1)
            self.print_step_detail(buffer, start, end, n-1)

    def tower_of_hanoi(self, n):
        print(self.count_step(n))
        self.print_step_detail(1,2,3,n)

s = Solution()
n = int(input())
s.tower_of_hanoi(n)