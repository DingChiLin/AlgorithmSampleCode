class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        result = []
        for i in range(len(nums)):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            if i >= k and deq[0] == i-k:
                deq.popleft()
            if i >= k-1:
                result.append(nums[deq[0]])
