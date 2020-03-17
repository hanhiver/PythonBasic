import decimal 

name = "Fred"
print(f"He said his name is {name}")

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f'result: {value:{width}.{precision}}')

