import asyncio
import threading

async def pr():
    print("In loop 2 thread 2")

def t():
    l2 = asyncio.new_event_loop()           #start new event loop on the new thread
    l2.run_until_complete(pr())

async def pr2():
    print("in loop 1 thread 1")
    t1 = threading.Thread(target = t,name="Thread 1")                       #start a new thread
    t1.start()
    t1.join()
    
if __name__ == "__main__":
    l1 = asyncio.new_event_loop()                       #start a new thread
    l1.run_until_complete(pr2())
    
