# 使用装饰器工厂函数，example函数的名称不会变成'wrapper'，
# 并且保留了原有函数的字符串文档。
from functools import wraps

def my_decorator(f):
    
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function.')
        return f(*args, **kwds)
    
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Call example function.')

example()
print(example.__name__)
print(example.__doc__)
