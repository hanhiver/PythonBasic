import logging
import logging.handlers

import time
import glob

LOG_FILENAME = 'logging_rotatingfile_example.out'

# 建立一个特定的logger，设定合适的logging level. 
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# 将特定的log message handler和logger连接起来。
handler = logging.handlers.RotatingFileHandler(
		LOG_FILENAME, 
		maxBytes = 20,
		backupCount = 5)
my_logger.addHandler(handler)

# 记录一些log messages. 
for i in range(20):
	my_logger.debug('i = %d' % i)

# 看看创建了哪些文件
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
	print(filename)
	