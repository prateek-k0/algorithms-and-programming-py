import asyncio
import time

async def fact(n):                                # sub task functions
    fact = 1
    print("Task 1 computing the factorial of ", n)
    for i in range(1,n+1):
        fact *= i
        await asyncio.sleep(0)                # task preemption
    print("Task 1 completed the computation of factorial of ", n)
    return fact

async def su(n):                                 # sub task functions
    s = 0
    print("Task 2 computing the sum upto ", n)
    for i in range(1,n+1):
        s += i
        await asyncio.sleep(0)                # task preemption
    print("Task 2 completed the computation of sum upto ", n)
    return s


async def task1():                                          # task functions which compute the results of sub task factorial
   f1 = asyncio.ensure_future(fact(4))
   f2 = asyncio.ensure_future(fact(6))
   f3 = asyncio.ensure_future(fact(10))
   print("Task 1 initiating . . . ",end = '\n')
   await asyncio.wait( [f1,f2,f3] )
   print("Task 1 finishing . . . ",end = '\n')
   return f1.result(), f2.result(), f3.result()

async def task2():                                          # task functions which compute the results of sub task sum asynchronously
   s1 = asyncio.ensure_future(su(4))
   s2 = asyncio.ensure_future(su(6))
   s3 = asyncio.ensure_future(su(10))
   print("Task 2 initiating . . . ",end = '\n')
   await asyncio.wait( [s1,s2,s3] )
   print("Task 2 finishing . . . ",end = '\n')
   return s1.result(), s2.result(), s3.result()

async def main_task():                                  # main task which computes the task functions asynchronously
    t1 = asyncio.ensure_future(task1())
    t2 = asyncio.ensure_future(task2())
    await asyncio.wait( [t1,t2] )
    return t1,t2

if __name__ == '__main__' :
    try:
       loop = asyncio.get_event_loop()
       mt = loop.create_task(main_task())       # main_task future object or task object
       tr1,tr2 = loop.run_until_complete(mt)
       print(tr1.result())                                    #results of each sub task
       print(tr2.result())
    finally:
        loop.close()
