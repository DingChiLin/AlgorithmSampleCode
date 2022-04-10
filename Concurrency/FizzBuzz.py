from threading import RLock, Lock, Thread

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.curr = 1
        self.mutex_fizz = Lock()
        self.mutex_buzz = Lock()
        self.mutex_fizz_buzz = Lock()
        self.mutex_number = Lock()
        self.mutex_fizz.acquire()
        self.mutex_buzz.acquire()
        self.mutex_fizz_buzz.acquire()
        self.mutex_number.acquire()

    def lock_fun(self, mutex, print):
        while self.curr <= self.n:
            mutex.acquire()
            if self.curr > self.n:
                return
            print()
            self.curr += 1
            self.mutex_number.release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz) -> None:
        self.lock_fun(self.mutex_fizz, printFizz)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz) -> None:
        self.lock_fun(self.mutex_buzz, printBuzz)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz) -> None:
        self.lock_fun(self.mutex_fizz_buzz, printFizzBuzz)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber) -> None:
        while self.curr <= self.n:
            if self.curr % 15 == 0:
                self.mutex_fizz_buzz.release()
                self.mutex_number.acquire()
            elif self.curr % 3 == 0:
                self.mutex_fizz.release()
                self.mutex_number.acquire()
            elif self.curr % 5 == 0:
                self.mutex_buzz.release()
                self.mutex_number.acquire()
            else:
                printNumber(self.curr)
                self.curr += 1

        self.curr += 1
        self.mutex_fizz.release()
        self.mutex_buzz.release()
        self.mutex_fizz_buzz.release()

def printFizz():
    print("Fizz")

def printBuzz():
    print("Buzz")

def printFizzBuzz():
    print("FizzBuzz")

def printNumber(n):
    print(n)

fb = FizzBuzz(20)
t1 = Thread(target=fb.fizz, args=(printFizz,))
t2 = Thread(target=fb.buzz, args=(printBuzz,))
t3 = Thread(target=fb.fizzbuzz, args=(printFizzBuzz,))
t4 = Thread(target=fb.number, args=(printNumber,))
t1.start()
t2.start()
t3.start()
t4.start()