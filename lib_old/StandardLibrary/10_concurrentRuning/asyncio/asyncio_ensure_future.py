import asyncio 

async def wrapped():
	print('wrapped')
	return 'result'

async def inner(task):
	print('inner: starting')
	print('inner: waiting for {!r}'.format(task))
	result = await task 
	print('inner: task returned {!r}'.format(result))

async def starter():
	print('starter: create task')
	task = asyncio.ensure_future(wrapped())
	print('starter: wait for inner')
	await inner(task)
	print('starter: inner returned')

envent_loop = asyncio.get_event_loop()

try:
	envent_loop.run_until_complete(starter())
finally: 
	envent_loop.close()

