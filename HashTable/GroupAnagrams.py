from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            m[key].append(str)
        return list(m.values())
            