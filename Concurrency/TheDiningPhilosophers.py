import threading
class DiningPhilosophers:
    def __init__(self):
        self.totalLock = threading.Semaphore(4)
        self.forkLock = [threading.Lock() for i in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        if self.totalLock.acquire():
            forkLock1, forkLock2 = self.forkLock[philosopher], self.forkLock[(philosopher + 1) % 5]
            if forkLock1.acquire() and forkLock2.acquire():
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
                forkLock1.release()
                forkLock2.release()
            self.totalLock.release()