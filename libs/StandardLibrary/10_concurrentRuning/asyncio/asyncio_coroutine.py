import asyncio

async def coroutine():
	print('in coroutine')

event_loop = asyncio.get_event_loop()

try:
	print('Starting coroutine')
	coro = coroutine()
	print('Entering event loop')
	event_loop.run_until_complete(coro)
finally:
	print('Closeing event loop')
	event_loop.close()

