import asyncio
from concurrent import futures
import time


async def one():
    print('Inside task 1... ')
    time.sleep(0.2)
    print('Starting worker thread ... ')
    with futures.ThreadPoolExecutor(max_workers = 1) as pool: # starts the pool, and then switches to next coroutine,
                                                              # thereby ensuring, parallel execution
        await asyncio.get_event_loop().run_in_executor(pool, thread_task)
    print('Finished task 1')

async def two():
    
    print('Inside task 2... ')
    for i in range(10):
        print(i+11)
    print('Finished task 2')

def thread_task():
    print('Inside worker thread task')
    for i in range(10):
        print(i)


if __name__ == '__main__' :
    tasks = [asyncio.ensure_future(one()), asyncio.ensure_future(two())]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

    
