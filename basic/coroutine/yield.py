"""
①创建generator对象：
包含yield表达式的函数将不再是一个函数，调用之后将会返回generator对象

②启动generator：
使用生成器之前需要先调用__next__或者send(None)，否则将报错。
启动generator后，代码将执行到yield出现的位置，也就是执行到yield n，
然后将n传递到generator.__next__()这行的返回值。（注意，生成器执行到yield n后将暂停在这里，直到下一次生成器被启动）

③发送值给yield表达式：
调用send方法可以发送值给yield表达式，同时恢复生成器的执行。
生成器从上次中断的位置继续向下执行，然后遇到下一个yield，生成器再次暂停，切换到主函数打印出send_result。
"""

def test():
    print("generator start")
    n = 1
    while True:
        res = yield n 
        print("RES: ", res)
        n += 1 

# 创建generator对象
generator = test()
print(type(generator))

print("-"*10)

# 启动generator
next_res = generator.__next__()
print("Next RES: ", next_res)

print("-"*10)

# 发送value给yield表达式
send_res = generator.send(123)
print("Send RES: ", send_res)

next_res = generator.send("Hello")
print("Next RES: ", next_res)

