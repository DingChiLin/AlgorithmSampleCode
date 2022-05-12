from threading import Condition
from threading import Thread
from threading import current_thread
import time
import random


class ReadersWriteLock():

    def __init__(self):
        self.cond_var = Condition()
        self.write_in_progress = False
        self.readers = 0

    def acquire_read_lock(self):
        self.cond_var.acquire()

        while self.write_in_progress is True:
            self.cond_var.wait()

        self.readers += 1
        print("reader count:", self.readers)

        self.cond_var.release()

    def release_read_lock(self):
        self.cond_var.acquire()

        self.readers -= 1
        if self.readers is 0:
            self.cond_var.notifyAll()

        self.cond_var.release()

    def acquire_write_lock(self):
        self.cond_var.acquire()

        while self.readers is not 0 or self.write_in_progress is True:
            self.cond_var.wait()
        self.write_in_progress = True

        self.cond_var.release()

    def release_write_lock(self):
        self.cond_var.acquire()

        self.write_in_progress = False
        self.cond_var.notifyAll()

        self.cond_var.release()


def writer_thread(lock):
    while True:
        lock.acquire_write_lock()
        print("\n{0} writing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                      lock.readers), flush=True)
        write_for = random.randint(1, 5)
        time.sleep(write_for)
        print("\n{0} releasing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.readers),
              flush=True)
        lock.release_write_lock()
        time.sleep(1)


def reader_thread(lock):
    while True:
        lock.acquire_read_lock()
        print("\n{0} reading at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.write_in_progress), flush=True)
        read_for = random.randint(1, 2)
        time.sleep(read_for)
        print("\n{0} releasing at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                          lock.write_in_progress), flush=True)
        lock.release_read_lock()
        time.sleep(1)


if __name__ == "__main__":

    lock = ReadersWriteLock()

    writer1 = Thread(target=writer_thread, args=(lock,), name="writer-1", daemon=True)
    writer2 = Thread(target=writer_thread, args=(lock,), name="writer-2", daemon=True)
    readers = list()
    for i in range(0, 3):
        readers.append(Thread(target=reader_thread, args=(lock,), name="reader-{0}".format(i + 1), daemon=True))

    writer1.start()
    for reader in readers:
        reader.start()
    writer2.start()

    time.sleep(15)
