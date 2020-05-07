def print_all(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    print()

print_all('lee',1234)
print_all('lee',1,2,3,4,5)
print_all('lee',1,2,3,4,5,like = 'python')
6