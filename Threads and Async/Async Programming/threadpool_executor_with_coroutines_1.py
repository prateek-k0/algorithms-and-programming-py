import asyncio
import time
import concurrent.futures as f

def blocking_task():                          # blocking tasks that require the use of a Thread pool
    print("Starting blocking tasks . . .  ")
    time.sleep(0.5)
    print("Processing . . ")
    time.sleep(3)
    print("Finishing blocking tasks . . .")
    time.sleep(0.5)


async def main_task_1():
    print("Starting main task 1 . . .")
    loop = asyncio.get_event_loop()
    with f.ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool,blocking_task)                          # release control to event loop with the help of 'await' keyword,
                                                                                                           #  the event loop shall switch to other coroutine
    print("Finishing main task 1 . . .")
    return

async def main_task_2():
    print("Starting main task 2 . . .")
    print("Starting now . . . ")
    await asyncio.sleep(0.4)
    print("Finishing main task 2 . . .")
    return

loop  = asyncio.new_event_loop()
loop.run_until_complete(asyncio.wait([main_task_1(),main_task_2()]))
loop.close()
