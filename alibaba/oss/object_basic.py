import oss2 
from itertools import islice

auth = oss2.Auth('AK'', 'ASK')
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'dhan-test')

for b in islice(oss2.ObjectIterator(bucket), 10):
    print(b.key)