'''
General Logging module for highway project. 

This module provide two level of logging system. 

1. Logging system inside one process. 
2. Logging system across different processes. 
	a. A logging threads read log messages from the pipe and log to the files. 
	b. A client call that generate log messages inside different processes. 

'''

import logging
import logging.handlers

import time
import glob

############################
### Local Logging system ###
############################

class SingleProcessLogger():

	def __init__(filename, 
				 log_level = logging.WARNING, 
				 max_bytes = 500, 
				 backup_count = 5):

		self.file_handler = logging.handlers.RotatingFileHandler(
							filename, maxBytes = max_bytes, backupCount = backup_count)
		self.stream_handler = logging.StreamHandler()
		self.formatter = logging.Formatter('%(asctime)s <%(threadName)s>: %(message)s')

	def get_logger(module, 
				   log_level = logging.WARNING, 
				   log_formatter = self.formatter):

		# Get a default Logger. 
		new_logger = logging.getLogger(module)

		# Associate the logger to file_handler and stream_handler. 
		new_logger.addHandler(self.file_handler)
		new_logger.addHandler(self.stream_handler)

		# Associate the default formatter to the logger. 
		new_logger.setFormatter(log_formatter)

######################################
### Multi-Processes Logging system ###
######################################




				

