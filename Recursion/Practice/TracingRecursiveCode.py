'''
Practice 1
'''
def func1(n):
    print(n)
    if n == 0:
        return
    func1(n-1)

func1(3)

'''
Practice 2
'''
# def func2(n):
#     if n == 0:
#         return
#     print(n)
#     func2(n-1)

# func2(3)

'''
Practice 3
'''
# def func3(n):
#     if n == 0:
#         return
#     func3(n-1)
#     print(n)

# func3(3)

'''
Practice 4
'''
# def func4(n):
#     print(n)
#     if n == 0:
#         return
#     print(n)
#     func4(n-1)
#     print(n)

# func4(3)

'''
Practice 5
'''
# def func5(n):
#     if n == 0:
#         return
#     print(n % 2)
#     return func5(n//2)

# print(func5(4))
# print(func5(8))
# print(func5(10))
# print(func5(13))

'''
Practice 6
'''
# def func6(nums, left, right):
#     if left >= right:
#         return
#     print(nums[left], nums[right])
#     return func6(nums, left + 1, right - 1)

# nums = [1,2,3,4,5,6]
# print(func6(nums, 0, len(nums)-1))