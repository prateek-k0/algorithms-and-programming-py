import asyncio
import time
import concurrent.futures as f

def blocking_tasks(i):                                                                                          # blocking tasks
    print("Starting blocking task {} . . . ".format(i))
    time.sleep(0.5)
    print("Processing . . ")
    time.sleep(3)
    print("Finishing blocking tasks . . .")
    time.sleep(0.5)

async def mt1():
    print("Starting main task 1 . . . ")
    loop = asyncio.get_event_loop()
    with f.ThreadPoolExecutor() as pool :
        await asyncio.wait([loop.run_in_executor(pool,blocking_tasks,i) for i in range(10)])                       #  yields control to the execution loop,
                                                                                                                                                            # for execution of another coroutine
    print("Finishing main task 1 . . .")
    return

async def mt2():
    print("Starting main task 2 . . .")
    print("Starting now . . . ")
    await asyncio.sleep(0)
    print("Finishing main task 2 . . .")
    return

loop = asyncio.new_event_loop()
loop.run_until_complete(asyncio.wait([mt1(),mt2()]))
loop.close()
