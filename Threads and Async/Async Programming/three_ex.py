import asyncio


async def one(n):
    print("Executing function 1, "+str(n))

async def two():
    loop = asyncio.new_event_loop()
    obj = loop.create_task(one('obj1'))
    obj2 = asyncio.ensure_future(one('obj2'))
    print("Executing function 2")

if __name__ == '__main__':
    asyncio.run(two())
