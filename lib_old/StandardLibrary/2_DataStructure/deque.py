import collections
import threading
import time

candle = collections.deque(range(10))

def burn(direction, nextSource):
	while True:
		try: 
			next = nextSource()
		except IndexError:
			break
		else:
			print('Burn the candel from < {:6}> value {}'.format(direction, next))
			time.sleep(0.2)

leftThread = threading.Thread(target = burn, args = ('LEFT', candle.popleft))
rightThread = threading.Thread(target = burn, args = ('RIGHT', candle.pop))

leftThread.start()
rightThread.start()

leftThread.join()
rightThread.join()

print('Burned out.')

