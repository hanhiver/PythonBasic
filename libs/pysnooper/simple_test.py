import pysnooper 

@pysnooper.snoop()
def demo_func():
    profile = {}
    profile['name'] = '寒冬的测试'
    profile['age'] = 100
    profile['lover'] = 'wcbb'

    return profile

def main():
    profile = demo_func()

if __name__ == "__main__":
    main()
