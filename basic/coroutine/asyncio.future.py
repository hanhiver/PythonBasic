import asyncio 

future = asyncio.Future()

async def coro1():
    print("Wait 1 second. ")
    await asyncio.sleep(1)
    print("set_result")
    future.set_result('data')

async def coro2():
    result = await future 
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([coro2(), coro1()]))

loop.close()

