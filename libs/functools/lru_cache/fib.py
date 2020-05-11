# 通过LRU_CACHE缓存函数的调用结果，
# 在下次相同调用的时候直接返回结果以节省时间。
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n 
    return fib(n-1) + fib(n-2)

fib_list = [fib(n) for n in range(24)]
print(fib_list)

# 通过cache_info()可以输出缓存的统计结果。
print(fib.cache_info())
