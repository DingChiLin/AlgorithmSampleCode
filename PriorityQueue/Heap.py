# Min Heap
class Heap():
    def __init__(self):
        self.list = [] # [[key, value], [key, value], ...] heapify by value
        self.mapping = {} #{key => index}
        return

    def __str__(self):
        return ','.join([str(v[1]) for v in self.list])

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):
        return self.list[key][1]

    def _swap(self, id1, id2):
        self.list[id1], self.list[id2] = self.list[id2], self.list[id1]
        self.mapping[self.list[id1][0]] = id1
        self.mapping[self.list[id2][0]] = id2

    def _parent(self, index):
        if index > 0:
            return (index-1) // 2
        else:
            return None
    
    def _left(self, index):
        return (index + 1) * 2 - 1
    
    def _right(self, index):
        return (index + 1) * 2

    def _bubble_up(self, index):
        parent = self._parent(index)
        while parent != None and self.list[index][1] < self.list[parent][1]:
            self._swap(parent, index)
            index = parent
            parent = self._parent(index)

    def _bubble_down(self, index):
        N = len(self.list)
        while index < N:
            left = self._left(index)
            right = self._right(index)
            flag = None
            if left >= N and right >= N:
                break
            elif left >= N:
                flag = 'right'
            elif right >= N:
                flag = 'left'
            else:
                if self.list[left][1] > self.list[right][1]:
                    flag = 'right'
                else:
                    flag = 'left'
            if flag == 'right':
                if self.list[index][1] > self.list[right][1]:
                    self._swap(index, right)
                    index = right
                else:
                    break
            elif flag == 'left':
                if self.list[index][1] > self.list[left][1]:
                    self._swap(index, left)
                    index = left
                else:
                    break

    def _remove(self, index):
        N = len(self.list)
        self._swap(index, N-1)
        res = self.list.pop()
        del self.mapping[res[0]]
        self._bubble_down(index)
        return res[1]              

    def pprint(self):
        print('list:', self.list)
        print('mapping:', self.mapping)

    def get(self, key):
        return self.list[self.mapping[key]][1]

    def values(self):
        return [v[1] for v in self.list]

    def append(self, key, value):
        self.list.append([key, value])
        index = len(self.list) - 1
        self.mapping[key] = index
        self._bubble_up(index)

    def pop(self, key = None):
        if not key:
            return self._remove(0)
        elif key not in self.mapping:
            return False
        else:
            return self._remove(self.mapping[key])

    def update(self, key, value):
        index = self.mapping[key]
        originValue = self.list[index][1]
        self.list[index] = [key, value]
        if value > originValue:
            self._bubble_down(index)
        elif value < originValue:
            self._bubble_up(index)

'''
Test
'''
# Test input and pop:
heap = Heap()
heap.append('e',5)
heap.append('g',7)
heap.append('f',6)
heap.append('d',4)
heap.append('b',2)
heap.append('c',3)
heap.append('a',1)
print(heap.list == [['a', 1], ['d', 4], ['b', 2], ['g', 7], ['e', 5], ['f', 6], ['c', 3]])
print(heap.mapping == {'e': 4, 'g': 3, 'f': 5, 'd': 1, 'b': 2, 'c': 6, 'a': 0})
print(heap.pop() == 1)
print(heap.pop() == 2)
print(heap.pop() == 3)
print(heap.list == [['d', 4], ['e', 5], ['f', 6], ['g', 7]])
print(heap.mapping == {'e': 1, 'g': 3, 'f': 2, 'd': 0})

# Test sorting
import random
heap2 = Heap()
lst = [i for i in range(100)]
expect = lst[:]
random.shuffle(lst)
for n in lst:
    heap2.append(n, n)
result = []
while len(heap2):
    result.append(heap2.pop())
print(result == expect)

# Test remove by key
heap3 = Heap()
heap3.append('e',5)
heap3.append('g',7)
heap3.append('f',6)
heap3.append('d',4)
heap3.append('b',2)
heap3.append('c',3)
heap3.append('a',1)
heap3.append('h',8)
heap3.append('i',9)
heap3.append('j',10)
heap3.pop('b') # remove 2
print(heap3.list == [['a', 1], ['d', 4], ['c', 3], ['g', 7], ['e', 5], ['f', 6], ['j', 10], ['h', 8], ['i', 9]])
print(heap3.mapping == {'e': 4, 'g': 3, 'f': 5, 'd': 1, 'c': 2, 'a': 0, 'h': 7, 'i': 8, 'j': 6})
heap3.pop('d') # remove 4
print(heap3.list == [['a', 1], ['e', 5], ['c', 3], ['g', 7], ['i', 9], ['f', 6], ['j', 10], ['h', 8]])
print(heap3.mapping == {'e': 1, 'g': 3, 'f': 5, 'c': 2, 'a': 0, 'h': 7, 'i': 4, 'j': 6})
heap3.pop('z') # not exist
print(heap3.list == [['a', 1], ['e', 5], ['c', 3], ['g', 7], ['i', 9], ['f', 6], ['j', 10], ['h', 8]])
print(heap3.mapping == {'e': 1, 'g': 3, 'f': 5, 'c': 2, 'a': 0, 'h': 7, 'i': 4, 'j': 6})

# Test remove all
import random
heap3 = Heap()
lst = [i for i in range(100)]
random.shuffle(lst)
for n in lst:
    heap3.append(str(n), n)
result = []
for n in [i for i in range(100)]:
    heap3.pop(str(n))
print(heap3.list == [])
print(heap3.mapping == {})

#Test update value of key

heap4 = Heap()
heap4.append('e',5)
heap4.append('g',7)
heap4.append('f',6)
heap4.append('d',4)
heap4.append('b',2)
heap4.append('c',3)
heap4.append('a',1)
heap4.append('h',8)
heap4.append('i',9)
heap4.append('j',10)
heap4.update('d', 6) # update 'd' => 6
print(heap4.list == [['a', 1], ['e', 5], ['b', 2], ['g', 7], ['d', 6], ['f', 6], ['c', 3], ['h', 8], ['i', 9], ['j', 10]])
print(heap4.mapping == {'e': 1, 'g': 3, 'f': 5, 'd': 4, 'b': 2, 'c': 6, 'a': 0, 'h': 7, 'i': 8, 'j': 9})
heap4.update('i', 3) # update 'i' => 3
print(heap4.list == [['a', 1], ['i', 3], ['b', 2], ['e', 5], ['d', 6], ['f', 6], ['c', 3], ['h', 8], ['g', 7], ['j', 10]])
print(heap4.mapping == {'e': 3, 'g': 8, 'f': 5, 'd': 4, 'b': 2, 'c': 6, 'a': 0, 'h': 7, 'i': 1, 'j': 9})
print(heap4[0] == 1)