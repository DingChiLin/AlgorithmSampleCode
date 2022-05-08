import threading
import time
 
num = 0
mutex = threading.Lock()

def func(st):
    global num
    print (threading.currentThread().getName(), "try to acquire the lock")
    if mutex.acquire():
        print (threading.currentThread().getName(), "acquire the lock")
        print (threading.currentThread().getName(), num)
        num += 1
        time.sleep(st)
        print (threading.currentThread().getName(), "release the lock.")       
        mutex.release()

# the same as func1
def func2(st):
    global num
    print (threading.currentThread().getName(), "try to acquire the lock")
    with mutex:
        print (threading.currentThread().getName(), "acquire the lock")
        print (threading.currentThread().getName(), num)
        num += 1
        time.sleep(st)
        print (threading.currentThread().getName(), "release the lock.")       
 
t1 = threading.Thread(target=func2, args=(8,))
t2 = threading.Thread(target=func2, args=(4,))
t3 = threading.Thread(target=func2, args=(2,))
t1.start()
t2.start()
t3.start()

