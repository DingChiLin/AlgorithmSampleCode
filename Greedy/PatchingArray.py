from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        last = 0
        add_cnt = 0
        for num in nums:
            if num <= last + 1:
                last += num
            else:
                # need add number
                while num > last + 1 and last < n:
                    last += (last + 1)
                    add_cnt += 1
                last += num
            if last >= n:
                break
        while n > last:
            last += (last + 1)
            add_cnt += 1
        return add_cnt

s = Solution()
nums = [1,3]
n = 6

nums = [1,2,31,33]
n = 2147483647

nums = [1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94]
n = 20
print(s.minPatches(nums, n))