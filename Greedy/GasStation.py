from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        diff = [gas[i] - cost[i] for i in range(N)]
        
        start_pos = 0
        partial_sum = 0
        total = 0
        for i in range(N):
            partial_sum += diff[i]
            if partial_sum < 0:
                total += partial_sum
                start_pos = i+1
                partial_sum = 0
        total += partial_sum
        
        return -1 if total < 0 else start_pos % N