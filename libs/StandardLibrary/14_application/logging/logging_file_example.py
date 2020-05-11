import time
import logging

LOG_FILENAME = 'logging_example.out'


logging.basicConfig(filename = LOG_FILENAME, level = logging.DEBUG,)

now = int(time.time())
time_array = time.localtime(now)
time_str = time.strftime(' %Y-%m-%d %H:%M:%S ', time_array)

logging.debug(time_str + ': This message should go to the log file. ')

with open(LOG_FILENAME, 'rt') as f:
	body = f.read()

print('FILE: ')
print(body)

