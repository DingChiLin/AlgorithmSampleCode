from typing import List
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1
        max_cnt = max(counter.values())
        tasks_have_max_cnt = len([c for c in counter.values() if c == max_cnt])

        return max(len(tasks), (max_cnt - 1) * (n + 1) + tasks_have_max_cnt)

s = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(s.leastInterval(tasks, n))