import asyncio
import time
import random

items = []

async def consumer():
    global items
    for i in range(1,11):
        if len(items) == 0:                     # check if the buffer is empty. . . if yes, then release control to the event loop            
            print("Cosnumer : No items to consume . . . entering in a state of halt . . .")
            await asyncio.sleep(0.1)          
        a = items.pop()
        print("Consumer : Item {} consumed from the buffer ".format(a))
        if i%2 == 0:        
            print("Cosnumer : Entering in a state of halt . . .")
            await asyncio.sleep(0.1)                    # after consuming 2 items, halt and release control to the event loop
                 

async def producer():
    global items
    for i in range(1,11):
        if len(items) > 5:                          # check if the buffer is full . . . if yes, then release control to the event loop            
            print("Producer   : The buffer is full . . . entering in a state of halt . . .")
            await asyncio.sleep(0.1)
        a = random.randint(101,999)
        items.append(a)
        print("Producer   : Item {} produced into the buffer ".format(a))
        if i % 5 == 0:
            print("Producer   : Entering in a state of halt . . .")
            await asyncio.sleep(0.1)                # after producing 5 items, halt and release control to the event loop

async def driver():                                 # driver function for producer and consumer function
        con = asyncio.ensure_future( consumer() )
        pro = asyncio.ensure_future( producer() )
        await asyncio.wait( [con,pro] )
        return

if __name__ == '__main__':
    try:
        a = time.time()
        loop = asyncio.get_event_loop()
        d_task = asyncio.ensure_future( driver() )
        loop.run_until_complete(d_task)
    finally:
        loop.close()
        print(time.time() - a)


