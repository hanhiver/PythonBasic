import decimal 
from datetime import datetime

name = "Fred"
print(f"He said his name is {name}")
# !r意味着对于变量先调用repr()再输出。
print(f"He said his name is {name!r}")

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")

today = datetime(year=2020, month=1, day=27)
# 使用特殊的Date格式
print(f"{today:%B %d, %Y}")

number = 1024
# 转换为十六进制特定格式
print(f"{number:#0x}")
