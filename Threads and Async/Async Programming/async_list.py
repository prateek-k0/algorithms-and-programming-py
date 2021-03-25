import asyncio

async def agen(r):
    for i in range(r):
        yield i

async def pr(num):
    print(num)

async def main():
    await asyncio.wait( [pr(i) async for i in agen(20) if i %2 == 0] ) 
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete( main() )
    loop.close()
    
