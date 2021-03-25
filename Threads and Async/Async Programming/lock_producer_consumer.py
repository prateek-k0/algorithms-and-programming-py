import asyncio
import random
import time

buffer = []
async def consumer(n,lock):
    global buffer
    for i in range(1,6):
        if len(buffer) == 0:
            print('Consumer {} : Buffer is empty. Waiting for items . . . '.format(n))
            await asyncio.sleep(0)
        async with lock:
            item = buffer.pop()
            print('Consumer {} : consumed item {} from the buffer. '.format(n,item))
        if i%2 == 0:
            print("Consumer {} : Entering in a halt . . .".format(n))
            await asyncio.sleep(0)
    return

async def producer(lock):
    global buffer
    for i in range(1,6):
        if len(buffer) >= 5:
            print('Producer : Buffer is full. Waiting . . . ')
            await asyncio.sleep(0.0000000001)
        async with lock:
            a = random.randint(101,999)
            buffer.append(a)
            print('Producer : produced item {} into the buffer. '.format(a))
    return

lock = asyncio.Lock()
asyncio.get_event_loop().run_until_complete(asyncio.wait([producer(lock), consumer(1,lock), consumer(2,lock)]))
