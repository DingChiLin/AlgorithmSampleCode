'''
For range max
1. Build: O(N)
2. Query: O(logN) 
3. Insert/Update: O(logN)  # insert could be O(1), but will need to maintain a prefixSum array
'''

'''
Important: 
1. Can only query the range start from beginning (prefixMax)
2. Can not support decreasing value
'''

class BinaryIndexedTree():
    def __init__(self, N):
        self.data = [0 for _ in range(N+1)]
        self.bit = [0 for _ in range(N+1)]

    # can only increasing
    def update(self, index, value):
        self.data[index] = value
        index += 1
        N = len(self.data)
        while index <= N:
            self.bit[index] = max(self.bit[index], value)
            index += (index & -index)

    def add(self, index, value):
        self.update(index, self.data[index] + value)

    def prefixMax(self, index):
        index += 1
        ans = 0
        while index != 0:
            ans = max(ans, self.bit[index])
            index -= (index & -index)
        return ans

bit = BinaryIndexedTree(9)
bit.add(1, 5)
bit.add(3, 7)
bit.add(2, 8)
print(bit.prefixMax(0)) # 0
print(bit.prefixMax(1)) # 5
print(bit.prefixMax(2)) # 8
print(bit.prefixMax(3)) # 8
print(bit.prefixMax(4)) # 8
bit.add(4, 9)
print(bit.prefixMax(3)) # 8
print(bit.prefixMax(4)) # 9
bit.add(3, 3)
print(bit.prefixMax(3)) # 10
print(bit.prefixMax(4)) # 10
bit.update(3, 11)
print(bit.prefixMax(3)) # 11
print(bit.prefixMax(4)) # 11
bit.update(3, 12)
print(bit.prefixMax(3)) # 12
print(bit.prefixMax(4)) # 12