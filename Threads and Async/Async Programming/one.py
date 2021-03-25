import asyncio
import time
async def f1():
    print("Task 1 started the execution . . . ")
    print("Task 1 entering in a halt . . . ")
    await asyncio.sleep(10)
    print()
    print("Task 1 returning from a halt . . . ")
    print("Task 1 completing the execution. . . ")
    print("Task 1 completed ! ")
    return

async def f2():
    print()
    print("Task 2 started the execution . . . ")
    print("Task 2 entering in a halt . . . ")
    await asyncio.sleep(5)
    print()
    print("Task 2 returning from a halt . . . ")
    print("Task 2 completing the execution. . . ")
    print("Task 2 completed ! ")
    return

async def f3():
    print()
    print("Task 3 started the execution . . . ")
    print("Task 3 entering in a halt . . . ")
    await asyncio.sleep(5)
    print()
    print("Task 3 returning from a halt . . . ")
    print("Task 3 completing the execution. . . ")
    print("Task 3 completed ! ")
    return

async def main():
    tasks = [asyncio.ensure_future(f1()), asyncio.ensure_future(f2()), asyncio.ensure_future(f3()) ]
    await asyncio.wait(tasks)
    return
if __name__ == "__main__" :
    try:
        a = time.time()
        asyncio.run(main())
    finally:
        print()
        print("Duration: ")
        print(time.time() - a)

        

             
