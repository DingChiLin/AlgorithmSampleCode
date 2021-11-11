class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        presum = [0] * (N+1)
        for i in range(1, N+1):
            presum[i] = (presum[i-1] + nums[i-1]) % k
        
        records = defaultdict(int)
        for i in range(N+1):
            n = presum[i]
            if n in records and (i - records[n]) >= 2:
                return True
            if n not in records:
                records[n] = i
        return False