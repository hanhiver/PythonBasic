# @staticmethod将函数变为类型的一个附属函数。
# 静态方法，可以通过实例调用，也可以通过类直接调用。 

import random
class Sample:
    def __init__(self,name):
        self.name = name

    def get_name(self,age):
        # 通过类型实例调用
        if self.judge(age):
            return self.name
        else:
            return "the name is stupid"

    @staticmethod
    def judge(n):
        num = random.randint(1,100)
        return num - n > 0

if __name__ == "__main__":
    s = Sample('rocky')
    name = s.get_name(23)
    print(name)

    # 通过类型直接调用
    print(Sample.judge(30))