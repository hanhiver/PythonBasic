import time
def func1():
    print("func1")
    sum = 0
    for i in range(1000000):
        sum += i

def func2():
    print("func2")
    time.sleep(2)

func1()
func2()

