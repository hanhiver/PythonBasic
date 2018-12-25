import datetime

class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds = period)
		self.reset_time = datetime.now()
		self.quota = 0

	def __repr__(self):
		return 'Bucket (quota = %d)' % self.quota

def fill(buket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		bucket.quota = 0
		bucket.reset_time = now

	bucket.quota += amount

def deduct(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		return False

	if bucket.quota - amount < 0:
		return False

	bucket.quota -= amount
	return True 

bucket = Bucket(60)
fill(bucket, 100)
print(bucket)
