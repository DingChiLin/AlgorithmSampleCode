import threading 
from time import sleep
 
condition = threading.Condition() 

def foo(name):
    if condition.acquire():
        print("start:", name)
        condition.wait()
        print("finish")
        condition.release()

def bar():
    sleep(3)
    if condition.acquire():
        condition.notify_all()
        condition.release()
 
t1 = threading.Thread(target=foo, args=(1,))
t2 = threading.Thread(target=foo, args=(2,))
t3 = threading.Thread(target=bar, args=())
t1.start()
t2.start()
t3.start()
