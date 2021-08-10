from typing import List
from collections import deque

# Do it directly
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        N = len(sandwiches)
        i = 0
        for _ in range(10000): # since N <= 100, the total operation will not exceeded 100*100
            if i < N and queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                if not queue: # not more students
                    break
            else:
                n = queue.popleft()
                queue.append(n)
        return len(queue)

# A more efficient way
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        N = len(students)
        counter = {0: 0, 1: 0}
        for n in students:
            counter[n] += 1
        cnt = 0
        for n in sandwiches:
            if counter[n] > 0:
                counter[n] -= 1
                cnt += 1
            else:
                break
        return N - cnt

s = Solution()
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(s.countStudents(students, sandwiches))