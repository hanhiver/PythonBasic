import functools
def myfunc(a, b = 2):
	print('   Called myfunc with: ', (a, b))

# Show details of a callable object. 
def show_detail(name, f, is_partial = False):
	print('{}: '.format(name))
	print('   object: ', f)
	if not is_partial:
		print('   __name__: ', f.__name__)
	else: 
		print('   func: ', f.func)
		print('   args: ', f.args)
		print('   keywords: ', f.keywords)
	return

show_detail('myfunc', myfunc)
myfunc('a', 3)
print()

# Set a different default value for 'b', 
# but require the caller to provide 'a'. 
p1 = functools.partial(myfunc, b = 4)
show_detail('partial with named default', p1, True)
p1('passing a')
p1('override b', b = 5)
print()

# Set default values for both 'a' and 'b'.  
p2 = functools.partial(myfunc, 'default a', b = 99)
show_detail('partial with defaults', p2, True)
p2()
p2(b = 'overiede b')
print()

print('Insufficient arguments: ')
#p1()


