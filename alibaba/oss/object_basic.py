import oss2 
from itertools import islice

# AccessKey ID: LTAI4GJRZRRjpURD7nAerLwd
# AccessKey Secret: QxW133A6UP7QC4avCxvgG7xsu7ddjh

auth = oss2.Auth('LTAI4GJRZRRjpURD7nAerLwd', 'QxW133A6UP7QC4avCxvgG7xsu7ddjh')
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'dhan-test')

for b in islice(oss2.ObjectIterator(bucket), 10):
    print(b.key)
