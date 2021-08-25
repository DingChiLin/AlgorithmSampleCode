class MyCircularQueue:
    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.capacity = k
        self.count = 0
        self.nums = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.count += 1
            self.nums[self.tail] = value 
            self.tail = (self.tail + 1) % self.capacity
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.count -= 1
            self.head = (self.head + 1) % self.capacity
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return  -1
        else:
            return self.nums[self.head]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return  -1
        else:
            return self.nums[(self.tail - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
