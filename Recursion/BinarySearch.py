class BinarySearch:
    def bisectLeft(self, nums, target, left, right):
        if left >= right:
            return left
        mid = (left + right) // 2
        if nums[mid] >= target:
            return self.bisectLeft(nums, target, left, mid)
        else:
            return self.bisectLeft(nums, target, mid + 1, right)

    def bisectRight(self, nums, target, left, right):
        if left >= right:
            return left
        mid = (left + right) // 2
        if nums[mid] > target:
            return self.bisectRight(nums, target, left, mid)
        else:
            return self.bisectRight(nums, target, mid + 1, right)

bs = BinarySearch()
nums = [1,3,4,4,4,6,9]
print(bs.bisectLeft(nums, 0, 0, len(nums))) #0
print(bs.bisectLeft(nums, 1, 0, len(nums))) #0
print(bs.bisectLeft(nums, 2, 0, len(nums))) #1
print(bs.bisectLeft(nums, 4, 0, len(nums))) #2
print(bs.bisectLeft(nums, 9, 0, len(nums))) #6
print(bs.bisectLeft(nums, 11, 0, len(nums))) #7

print(bs.bisectRight(nums, 0, 0, len(nums))) #0
print(bs.bisectRight(nums, 1, 0, len(nums))) #1
print(bs.bisectRight(nums, 2, 0, len(nums))) #1
print(bs.bisectRight(nums, 4, 0, len(nums))) #5
print(bs.bisectRight(nums, 9, 0, len(nums))) #7
print(bs.bisectRight(nums, 11, 0, len(nums))) #7