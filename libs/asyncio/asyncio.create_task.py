import asyncio 
import time 

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def serial():
    print(f"Serial started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"Serial finished at {time.strftime('%X')}")

async def createTask():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"createTask started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"createTask finished at {time.strftime('%X')}")


# 串行运行。
asyncio.run(serial())

# 创建协程运行。
asyncio.run(createTask())
