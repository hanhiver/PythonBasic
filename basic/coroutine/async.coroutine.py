# python 3.4 的解决方案。
# asyncio.coroutine将会在3.8之后废除。
import asyncio 

@asyncio.coroutine
def compute(x, y):
    print("Compute %s + %s ..." %(x, y))
    yield from asyncio.sleep(1.0)
    return x + y 

@asyncio.coroutine
def print_sum(x, y):
    result = yield from compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
print("start")
loop.run_until_complete(print_sum(1, 2))
print("end")
loop.close()

