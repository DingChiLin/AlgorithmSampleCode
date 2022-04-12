from typing import List

class Solution:
    def __init__(self):
        self.buf4 = [""] * 4
        self.buf4Index = 0
        self.maxIndex = 0

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.buf4Index == self.maxIndex:
                self.buf4Index = 0
                self.maxIndex = read4(self.buf4)
                if self.maxIndex == 0:
                    break
            buf[i] = self.buf4[self.buf4Index]
            i += 1
            self.buf4Index += 1
        return i