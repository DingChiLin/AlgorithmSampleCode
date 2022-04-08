class Math:
    def gcd(self, x, y):
        if (y == 0):
            return x
        return self.gcd(y, x%y)

M = Math()
print(M.gcd(24, 16))