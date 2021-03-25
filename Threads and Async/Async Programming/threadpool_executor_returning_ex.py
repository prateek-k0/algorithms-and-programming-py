import asyncio
from concurrent import futures

async def mt():
    print('Inside main thread')
    await asyncio.sleep(0.1)
    return list(range(10))

async def st():
    await asyncio.sleep(0.1)
    print('Inside side thread')
    await asyncio.sleep(0.1)
    return list(range(10,20))

def stt():
    res = asyncio.new_event_loop().run_until_complete(st())
    return res

loop = asyncio.get_event_loop()
pool = futures.ThreadPoolExecutor(max_workers = 1)
sto = loop.run_in_executor(pool,stt)
completed,_ = loop.run_until_complete(asyncio.wait([mt(), sto]))
for task in completed:
    print(task.result())
