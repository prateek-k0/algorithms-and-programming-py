import asyncio
import functools

#async wrappers are particularly helpful when we want to create coroutines out of existing synchronous functions

def async_dec(func):
    @functools.wraps(func)
    async def wrapper(*args):
        print('Arguments passed: ')
        print(args)
        return func(*args)
    return wrapper

@async_dec
def myfunc(*args):
    return sum(args)


print(asyncio.get_event_loop().run_until_complete(myfunc(3,12)))
print()

    
#likewise, synchronous wrappers are useful for calling coroutines in normal fashion

def sync_dec(func):
	@functools.wraps(func)
	def wrapper(*args):
		print('Inside synchronous wrapper.....')
		asyncio.get_event_loop().run_until_complete(func(*args))
		print('Exiting')
	return wrapper

@sync_dec
async def myfunc2(*args):
	print('Sum is {}'.format(sum(args)))


myfunc2(7,8)
