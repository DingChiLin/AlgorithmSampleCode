from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastPosition = defaultdict(int)
        for i, c in enumerate(s):
            lastPosition[c] = i
        ans = []
        pre = -1
        last = 0
        for i, c in enumerate(s):
            last = max(last, lastPosition[c])
            if (last == i):
                ans.append(i - pre)
                pre = i
        return ans

s = Solution()
input = "ababcbacadefegdehijhklij"
print(s.partitionLabels(input))