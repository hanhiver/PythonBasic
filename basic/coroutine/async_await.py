# python 3.8 的解决方案。
import asyncio 

async def compute(x, y):
    print("Compute %s + %s ..." %(x, y))
    await asyncio.sleep(1.0)
    return x + y 

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
print("start")
loop.run_until_complete(print_sum(1, 2))
print("end")
loop.close()