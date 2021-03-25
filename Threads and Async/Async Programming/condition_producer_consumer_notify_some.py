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
    for i in range(1,11):
        async with condition:
            a = random.randint(101,999)
            buffer.append(a)
            print('Producer  :  produced item {} into the buffer'.format(a))
            if i%5 == 0:
                condition.notify(5)
                await asyncio.sleep(0.5)
    return

async def main():
    condition = asyncio.Condition()
    l = [ asyncio.create_task(consumer(condition,i)) for i in range(10) ]
    await asyncio.wait([asyncio.create_task(producer(condition))] + l)
    return

if __name__ == '__main__':
    #asyncio.run(main())
    await main()
    

    
