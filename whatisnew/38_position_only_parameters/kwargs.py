def func(a, b, /, **kwargs):
    print(a, b, kwargs)

# 调用里面将a,b使用了两次。
func(10, 20, a=1, b=2, c=3)
