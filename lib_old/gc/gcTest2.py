import gc 
import sys 

class CGcleak():
	def __init__(self):
		self._text = '#' * 10

	def __del__(self):
		pass 

def make_circle_ref():
	_gcleak = CGcleak()
	_gcleak._self = _gcleak # 自己循环引用自己。
	print('_gclean引用数目：', sys.getrefcount(_gcleak))

	del _gcleak 
	try:
		print('_gclean引用数目：', sys.getrefcount(_gcleak))
	except UnboundLocalError:
		print('_gcleak不存在。')

def test_gcleak():
	gc.enable()

	print('开始垃圾泄露测试...')
	make_circle_ref() 

	print('开始收集垃圾...')
	_unreachable = gc.collect()

	print('Unreachable object num: ', (_unreachable))
	print('Garbage object num: ', len(gc.garbage))

if __name__ == '__main__':
	test_gcleak()
