def print_kwargs(**kwargs):
    """kwargs包含了输入的所有参数构成的字典，参数的名字是字典的key，参数的内容是字典的value"""
    print(kwargs)

print_kwargs(a = 'lee',b = 'sir',c = 'man')