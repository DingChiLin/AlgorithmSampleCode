from threading import RLock, Lock, Thread

class Foo:
    def __init__(self):
        self.gate1 = Lock()
        self.gate2 = Lock()
        self.gate1.acquire()
        self.gate2.acquire()
        pass

    def first(self, printFirst) -> None:
        printFirst()
        self.gate1.release()

    def second(self, printSecond) -> None:
        with self.gate1:
            printSecond()
            self.gate2.release()
        # if self.gate1.acquire():
        #     printSecond()
        #     self.gate1.release()
        #     self.gate2.release()

    def third(self, printThird) -> None:
        with self.gate2:
            printThird()
        # if self.gate2.acquire():
        #     printThird()
        #     self.gate2.release()

def printFirst():
    print("first")

def printSecond():
    print("Second")

def printThird():
    print("Third")

foo = Foo()
t1 = Thread(target=foo.first, args=(printFirst,))
t2 = Thread(target=foo.second, args=(printSecond,))
t3 = Thread(target=foo.third, args=(printThird,))
t1.start()
t2.start()
t3.start()