import asyncio

async def foo():
    return 42

coro = asyncio.create_task(foo())
done, pending = await asyncio.wait({task})

if task in done:
    print('Done.')
    