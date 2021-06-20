def backtracking(n):
    if n > 3:
        return

    print(n)
    backtracking(n+1)
    print(n)

backtracking(1)

# def backtracking_1(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     new_nums = nums + [1]
#     backtracking_1(n+1, new_nums)

# backtracking_1(0, [])

# def backtracking_2(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     for i in range(1, 3): # 1, 2
#         new_nums = nums + [i]
#         backtracking_2(n + 1, new_nums)

# backtracking_2(0, [])

# def backtracking_2_b(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     for i in range(1, 3): # 1, 2
#         nums.append(i)
#         backtracking_2_b(n + 1, nums)
#         nums.pop()

# backtracking_2_b(0, [])

# def backtracking_3(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     for i in range(1, 4): # 1, 2, 3
#         new_nums = nums + [i]
#         backtracking_3(n + 1, new_nums)

# backtracking_3(0, [])

# def backtracking_3_b(n, nums):
#     print(nums)
#     if n >= 2:
#         return

#     for i in range(1, 4): # 1, 2, 3
#         nums.append(i)
#         backtracking_3_b(n + 1, nums)
#         nums.pop()

# backtracking_3_b(0, [])