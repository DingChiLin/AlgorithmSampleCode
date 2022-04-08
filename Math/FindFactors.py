from collections import defaultdict

class Math:
    def get_prime_factors(self, n):
        result = defaultdict(int)
        while n % 2 == 0:
            result[2] += 1
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                result[i] += 1
                n //= i
            i += 2

        if n > 2:
            result[n] += 1
        return result

M = Math()
print(M.get_prime_factors(2*2*3*3*3*7*11*13))
print(M.get_prime_factors(9))