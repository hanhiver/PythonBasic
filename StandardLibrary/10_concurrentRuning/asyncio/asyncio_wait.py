import asyncio

async def phase(i):
	print('in phase {}'.format(i))
	await asyncio.sleep(0.1 * i)
	print('done with phase {}'.format(i))
	return 'phase {} result'.format(i)

async def main(num_phases):
	print('starting main')

	phases = [phase(i) for i in range(num_phases)]

	print('waiting for phases to complete')

	complete, pending = await asyncio.wait(phases, timeout = 0.5)

	results = [t.result() for t in complete]
	print('results: {!r}'.format(results))

	if pending: 
		print('cancel the pending tasks')
		for t in pending:
			t.cancel()
			

event_loop = asyncio.get_event_loop()

try:
	event_loop.run_until_complete(main(8))
finally:
	event_loop.close()

