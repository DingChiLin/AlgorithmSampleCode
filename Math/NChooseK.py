from functools import lru_cache
class Math:
    @lru_cache(None)
    def choose(self, n, k):
        if k == 0:
            return 1
        k = min(k, n-k)
        return (n * self.choose(n - 1, k - 1)) // k

M = Math()
print(M.choose(100,30))