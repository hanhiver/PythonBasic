import pysnooper 

# 此处添加output会将输出重定向到日志文件。 
@pysnooper.snoop(output='/tmp/debug.log')
def demo_func():
    profile = {}
    profile['name'] = '寒冬的测试'
    profile['age'] = 100
    profile['lover'] = 'wcbb'

    return profile

def main():
    profile = demo_func()

if __name__ == "__main__":
    print('日志输出将会被重定向到/tmp/debug.log')
    main()
