import threading
import time

slock = threading.Semaphore(0)
item = 0

def consumer():
    global item
    ##consume an item
    slock.acquire()
    time.sleep(0.1)
    print("Item ", item, "consumed",end = '\n')
    print("Consumer Waiting")
    

def producer():
    global item
    item += 1
    ##produce an item to be consumed
    slock.release()
    print("Item ", item, "produced")

a = time.time()
for i in range(10):
    t2 = threading.Thread(target=producer)
    t1 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

print(time.time() - a)
