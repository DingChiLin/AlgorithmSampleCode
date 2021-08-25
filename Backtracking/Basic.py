'''
Basic
'''

def backtracking(n):
    if n > 3:
        return

#     print(n)
#     backtracking(n+1)
#     print(n)

# backtracking(1)

# def backtracking_1(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     new_nums = nums + [1]
#     backtracking_1(n+1, new_nums)

# backtracking_1(0, [])

'''
Digital Lock
'''

# def backtracking_digit_lock(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     for i in range(1, 3): # 1, 2
#         new_nums = nums + [i]
#         backtracking_digit_lock(n + 1, new_nums)

# def backtracking_2_b(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     for i in range(1, 3): # 1, 2
#         nums.append(i)
#         backtracking_2_b(n + 1, nums)
#         nums.pop()

# backtracking_2_b(0, [])

# def backtracking_digit_lock_3(n, nums):
#     if n >= 3:
#         print(nums)
#         return

#     for i in range(1, 4): # 1, 2, 3
#         nums.append(i)
#         backtracking_digit_lock_3(n + 1, nums)
#         nums.pop()

# backtracking_digit_lock_3(0, [])

'''
Combination
'''

# def backtracking_combination_1(n, start, nums):
#     if n >= 2:
#         print(nums)
#         return

#     for i in range(start, 4): # 1, 2
#         nums.append(i)
#         backtracking_combination_1(n + 1, i + 1, nums)
#         nums.pop()

# backtracking_combination_1(0, 1, [])

# def backtracking_combination_2(n, start, nums):
#     if n >= 3:
#         print(nums)
#         return

#     for i in range(start, 5): # 1, 2
#         nums.append(i)
#         backtracking_combination_2(n + 1, i + 1, nums)
#         nums.pop()

# backtracking_combination_2(0, 1, [])
