import threading 
import time 
 
condition = threading.Condition() 
products = 0 
 
class Producer(threading.Thread): 
    def __init__(self): 
        threading.Thread.__init__(self) 
 
    def run(self): 
        global condition, products 
        while True: 
            if condition.acquire(): 
                if products < 10: 
                    products += 1; 
                    print(f"Producer({self.name})):deliver one, now products:{products}")
                    condition.notify() 
                else: 
                    print(f"Producer({self.name}):already 10, stop deliver, now products: {products}")
                    condition.wait(); 
                condition.release() 
                time.sleep(2) 

class Consumer(threading.Thread): 
    def __init__(self): 
        threading.Thread.__init__(self) 
 
    def run(self): 
        global condition, products 
        while True: 
            if condition.acquire(): 
                if products > 1: 
                    products -= 1 
                    print(f"Consumer({self.name}):consume one, now products:{products}")
                    condition.notify() 
                else: 
                    print(f"Consumer({self.name}):only 1, stop consume, products:{products}")
                    condition.wait(); 
                condition.release() 
                time.sleep(2) 

if __name__ == "__main__": 
    for p in range(0, 5): 
        p = Producer() 
        p.start() 
 
    for c in range(0, 10): 
        c = Consumer() 
        c.start()