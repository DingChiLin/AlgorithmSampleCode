class BinarySearch:
    def bisectLeft(self, nums, target):
        left = 0
        right = len(nums)
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def bisectRight(self, nums, target):
        left = 0
        right = len(nums)
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

bs = BinarySearch()
nums = [1,3,4,4,4,6,9]
print(bs.bisectLeft(nums, 0)) #0
print(bs.bisectLeft(nums, 1)) #0
print(bs.bisectLeft(nums, 2)) #1
print(bs.bisectLeft(nums, 4)) #2
print(bs.bisectLeft(nums, 9)) #6
print(bs.bisectLeft(nums, 11)) #7

print(bs.bisectRight(nums, 0)) #0
print(bs.bisectRight(nums, 1)) #1
print(bs.bisectRight(nums, 2)) #1
print(bs.bisectRight(nums, 4)) #5
print(bs.bisectRight(nums, 9)) #7
print(bs.bisectRight(nums, 11)) #7