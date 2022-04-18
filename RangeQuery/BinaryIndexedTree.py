'''
For range sum
1. Build: O(N)
2. Query: O(logN) 
3. Insert/Update: O(logN)  # insert could be O(1), but will need to maintain a prefixSum array
'''

class BinaryIndexedTree():
    def __init__(self, data):
        self.data = data
        self.bit = self._build(data) # keep the total sum info of the data

    def _build(self, data):
        N = len(data)
        bit = [0 for i in range(N+1)]
        for i, n in enumerate(data):
            bit[i+1] = bit[i] + n

        for i in range(N, 0, -1):
            bit[i] -= bit[i - (i&-i)]
        return bit

    def values(self):
        return self.bit

    def insert(self, value):
        N = len(self.data)
        prefixSum = self.prefixSum(N-1)
        newIndex = N + 1
        newValue = prefixSum + value - self.prefixSum(newIndex - (newIndex & -newIndex) - 1)
        self.bit.append(newValue)
        self.data.append(value)

    def add(self, index, value): # add `value` to self.data[index]
        self.data[index] += value
        index += 1
        N = len(self.data)
        while index <= N:
            self.bit[index] += value
            index += (index & -index)

    def update(self, index, value): # update self.data[index] to value
        self.add(index, value - self.data[index])
        self.data[index] = value

    def prefixSum(self, index):
        index += 1
        ans = 0
        while index != 0:
            ans += self.bit[index]
            index -= (index & -index)
        return ans
    
    def query(self, left, right):
        return self.prefixSum(right) - self.prefixSum(left-1) if left > 0 else self.prefixSum(right)

data = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5, 9, 2, 7] # len(data) = 17
bit = BinaryIndexedTree(data)
print('-- prefix sum ---')
print(bit.prefixSum(0)) #1 index start from 0
print(bit.prefixSum(1)) #8
print(bit.prefixSum(2)) #11
print(bit.prefixSum(3)) #11
print(bit.prefixSum(4)) #16
print(bit.prefixSum(7)) #29
print(bit.prefixSum(12)) #43
print(bit.prefixSum(16)) #66 total sum
bit.add(3,3)
print(bit.prefixSum(4)) #19
bit.update(3,5)
print(bit.prefixSum(4)) #21
bit.update(3,100)
print(bit.prefixSum(0)) #1 index start from 0
print(bit.prefixSum(1)) #8
print(bit.prefixSum(2)) #11
print(bit.prefixSum(3)) #111
print(bit.prefixSum(4)) #116
print(bit.prefixSum(7)) #129
print(bit.prefixSum(12)) #143 
print(bit.prefixSum(16)) #166 total sum
bit.update(7,30)
print(bit.prefixSum(0)) #1 index start from 0
print(bit.prefixSum(1)) #8
print(bit.prefixSum(2)) #11
print(bit.prefixSum(3)) #111
print(bit.prefixSum(4)) #116
print(bit.prefixSum(7)) #157
print(bit.prefixSum(12)) #171
print(bit.prefixSum(16)) #194 total sum
print('-- range sum ---')
print(bit.query(0, 7)) #157
print(bit.query(3, 7)) #146 sum([100, 5, 8, 3, 30])
print('-- insert ---')
bit.insert(100)
print(bit.query(3, 7)) #146 not change
print(bit.query(3, 17)) #283 sum([100, 5, 8, 3, 30, 6, 2, 1, 1, 4, 5, 9, 2, 7, 100])
bit.insert(9)
print(bit.query(3, 18)) #292 sum([100, 5, 8, 3, 30, 6, 2, 1, 1, 4, 5, 9, 2, 7, 100, 9])
bit.insert(8)
print(bit.query(3, 17)) #283 sum([100, 5, 8, 3, 30, 6, 2, 1, 1, 4, 5, 9, 2, 7, 100])
print(bit.query(3, 18)) #292 sum([100, 5, 8, 3, 30, 6, 2, 1, 1, 4, 5, 9, 2, 7, 100, 9])
print(bit.query(3, 19)) #300 sum([100, 5, 8, 3, 30, 6, 2, 1, 1, 4, 5, 9, 2, 7, 100, 9, 8])