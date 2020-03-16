from datetime import date
from math import cos, radians

# f-strings比如f'{expr=}'会被自动展开。
user = 'eric'
member_since = date(2019, 9, 25)
fs = f'{user=} : {member_since=}'
print(fs)
# user='eric' : member_since=datetime.date(2019, 9, 25)

delta = date.today() - member_since
fs = f'{user=!s}  {delta.days=:,d}'
print(fs)
# user=eric  delta.days=174

theta = 30
print(f'{theta=}  {cos(radians(theta))=:.3f}')
# theta=30  cos(radians(theta))=0.866

