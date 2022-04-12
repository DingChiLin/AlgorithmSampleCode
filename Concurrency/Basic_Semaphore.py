import threading
import time

semaphore = threading.Semaphore(2)
 
def func():
    if semaphore.acquire():
        for i in range(5):
            print (threading.currentThread().getName(), "get semaphore")
        semaphore.release()
        print (threading.currentThread().getName(), "release semaphore")
 
for i in range(4):
    t1 = threading.Thread(target=func)
    t1.start()

