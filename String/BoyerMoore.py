from collections import defaultdict


class Solution:
    def strStr(self, document: str, target: str) -> int:
        N = len(target)
        if N > len(document):
            return -1
        if N == 0:
            return 0

        last_pos = defaultdict(lambda:-1)
        for i, c in enumerate(target):
            last_pos[c] = i

        i = N - 1
        while i < len(document):
            k = next(j for j in range(N + 1) if j == N or target[N - 1 - j] != document[i - j])
            if k == N: # get answer
                return i - (N - 1)
            else:
                i += max(1, N - 1 - last_pos[document[i]], N - 1 - k - last_pos[document[i - k]])

        return -1

document = "This is a simpeiampli for eiampli moore algorithm"
target = "eiampli"

# document = "aabaacaadaa"
# target = "aca"

# document = ""
# target = "a"

s = Solution()
print(s.strStr(document, target))