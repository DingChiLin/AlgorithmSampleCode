# 1.這個 function 會進來幾次 O(N)
# 2.每次花多少時間 O(N)
# 最終時間複雜度 O(N) * O(N) = O(N^2)
def reverseNums(nums): # [1,2,4,5,6]
    N = len(nums)
    if N == 1: # 終止條件
        return nums
    first = nums[0:N-1] # [1,2,4,5] 小一點的問題
    second = [nums[N-1]] # [6]
    reversedFirst = reverseNums(first) # 遞迴！ 理論上回傳值會是 [5,4,2,1]

    return second + reversedFirst # [6] + [5,4,2,1] = [6,5,4,2,1]

nums = [1,2,4,5,6]
print(reverseNums(nums))