import threading
import time

semaphore = threading.Semaphore(2)
 
def func():
    if semaphore.acquire():
        print(threading.currentThread().getName(), 'get semaphore')
        time.sleep(1)
        semaphore.release()
        print(threading.currentThread().getName(), 'release semaphore')
       
for i in range(10):
    t1 = threading.Thread(target=func)
    t1.start()