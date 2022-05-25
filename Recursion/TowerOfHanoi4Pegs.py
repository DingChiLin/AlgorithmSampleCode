class Solution:
    def count_step(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return 2 * self.count_step(n-2) + 3

    def print_step_detail(self, start, buffer1, buffer2, end, n):
        if n == 0:
            return
        if n == 1:
            print(start, end)
        else:
            self.print_step_detail(start, buffer2, end, buffer1, n-2)
            self.print_step_detail(start, buffer1, end, buffer2, 1)
            self.print_step_detail(start, buffer1, buffer2, end, 1)
            self.print_step_detail(buffer2, start, buffer1, end, 1)
            self.print_step_detail(buffer1, start, buffer2, end, n-2)

    def tower_of_hanoi_4_pegs(self, n):
        print(self.count_step(n))
        self.print_step_detail(1,2,3,4,n)

s = Solution()
n = int(input())
s.tower_of_hanoi_4_pegs(n)