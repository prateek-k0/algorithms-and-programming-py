import asyncio
import random
import time

buffer = []

async def consumer(condition,n):
    global buffer
    async with condition:
        print('Consumer {} is waiting . . .'.format(n))
        await condition.wait()
        print('Consumer {} consumed item {} from the buffer '.format(n,buffer.pop()))
    return

async def producer(condition):
    global buffer
    for i in range(1,6):
        async with condition:
            a = random.randint(101,999)
            buffer.append(a)
            print('Producer produced item {} into the buffer'.format(a))
    async with condition:
        condition.notify_all()
    return

async def main():
    loop = asyncio.get_event_loop()
    condition = asyncio.Condition()
    l = [ loop.create_task(consumer(condition,i)) for i in range(5) ]
    await asyncio.wait([loop.create_task(producer(condition))] + l)
    return

if __name__ == '__main__':
    asyncio.run(main())
    

    
