import pysnooper 

out = {"foo": "bar"}

# 此处添加watch对全局变量进行跟中。 
@pysnooper.snoop(watch=("out['foo']"))
def demo_func():
    profile = {}
    profile['name'] = '寒冬的测试'
    profile['age'] = 100
    out['foo'] = 'foobar'
    profile['lover'] = 'wcbb'

    return profile

def main():
    profile = demo_func()

if __name__ == "__main__":
    print('日志输出将会被重定向到/tmp/debug.log')
    main()
