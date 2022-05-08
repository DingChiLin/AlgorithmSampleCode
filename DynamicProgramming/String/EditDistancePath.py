'''
      t
    a b c
s a
  b
  c     
  t     
'''



def diffBetweenTwoStrings(source, target):
    N = len(source)
    M = len(target)
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    path = [[(None, None) for _ in range(M+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i][0] = i
        path[i][0] = (i-1, 0) 
    for j in range(1, M+1):
        dp[0][j] = j
        path[0][j] = (0, j-1) 
    for i in range(1, N+1):
        for j in range(1, M+1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
                path[i][j] = (i-1, j-1)
            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    path[i][j] = (i, j-1)
                    dp[i][j] = 1 + dp[i][j-1]
                else: # if it's equal
                    path[i][j] = (i-1, j)
                    dp[i][j] = 1 + dp[i-1][j]  

    final_path = []
    i = N
    j = M
    while i != None and j != None:
        final_path.append((i, j))
        i, j = path[i][j]

    ans = []
    #compare: final_path[i] and final_path[i-1]
    for i in range(1, len(final_path)):
        last = final_path[i-1] # N-1, M-1
        cur = final_path[i] # N-1, M-2
        if cur[0] == last[0] - 1 and cur[1] == last[1] - 1:
            ans.append(source[last[0]-1])
        elif cur[0] == last[0] - 1:
            ans.append('-' + source[last[0]-1])
        else: # cur[1] == last[1] - 1
            ans.append('+' + target[last[1]-1])

    ans = ans[::-1]
    return ans

source = "abct"
target = "abd"

source = "ABCDEFG"
target = "ABDFFGH"

# source = "AABACC"
# target = "BABCAC"
print(diffBetweenTwoStrings(source, target))