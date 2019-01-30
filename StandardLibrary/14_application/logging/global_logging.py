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

########################
# Local Logging system #
########################

class SingleProcessLogger():

	def __init__(filename, 
				 log_level = logging.WARNING, 
				 max_bytes = 500, 
				 backup_count = 5):

		self.logger = logging.getLogger('')

