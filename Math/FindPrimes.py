class Math:
    # Sieve of Eratosthenes 
    def get_prime(self, n):
        prime = [True for _ in range(n + 1)]
        prime[0] = False
        prime[1] = False
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p ** 2, n + 1, p):
                    prime[i] = False
            p += 1

        result = set()
        for p in range(n + 1):
            if prime[p]:
                result.add(p)

        return result

M = Math()
print(M.get_prime(101))