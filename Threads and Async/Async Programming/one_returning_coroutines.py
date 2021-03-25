import time
import asyncio

async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 1000 == 0:
            await asyncio.sleep(0)
            
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located
 
async def return_values():                                                                        # a function that helps to return the values from asynchronous functions
        loop = asyncio.get_event_loop()
        divs1 = loop.create_task(find_divisibles(508000, 34113))
        divs2 = loop.create_task(find_divisibles(100052, 3210))
        divs3 = loop.create_task(find_divisibles(500, 3))
        await asyncio.wait([divs1,divs2,divs3])                                            # wait till they complete the execution
        return divs1,divs2,divs3

if __name__ == "__main__":
    try:
        a = time.time()
        loop = asyncio.get_event_loop()
        ret_values_task = loop.create_task( return_values() )                       # create a task object of return_values function
        d1, d2, d3 = loop.run_until_complete( ret_values_task )                 # execute return_values function, or rather, execute its task object
        print(d1.result())                                                   # returns the result of execution of a task object   syntax - task_object.result()
    finally:
        loop.close()
        print(time.time() - a)

