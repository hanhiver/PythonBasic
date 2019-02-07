import asyncio

async def outer():
	print('In outer')
	print('Waiting for result1')
	result1 = await phase1()
	print('Waiting for result2')
	result2 = await phase2(result1)
	return (result1, result2)

async def phase1():
	print('In phase1')
	return 'res1'

async def phase2(arg):
	print('In phase2')
	return 'res2 derived from {}'.format(arg)

event_loop = asyncio.get_event_loop()

try:
	return_value = event_loop.run_until_complete(outer())
	print('Return value: {!r}'.format(return_value))
finally:
	event_loop.close()

