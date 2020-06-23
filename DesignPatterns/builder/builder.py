# 建造者模式
# 某类产品的构建由很多的复杂组件组成；
# 某些组件中的某些细节不同，构建出的产品表象会略有不同；
# 通过一个指挥者按照产品的创建步骤来一步步执行产品的创建；
# 当需要创建不同的产品时，只需要派生一个具体的建造者，重写相应的组件构建方法即可。

def printInfo(info):
    print(info)

# Builder的基类
class PersonBuilder():
    def BuildHead(self):
        pass

    def BuildBody(self):
        pass

    def BuildArm(self):
        pass

    def BuildLeg(self):
        pass 

# 胖子
class PersonFatBuilder(PersonBuilder):
    type = '胖子'
    def BuildHead(self):
        printInfo('构建%s的.....大头' % self.type)

    def BuildBody(self):
        printInfo('构建%s的身体' % self.type)

    def BuildArm(self):
        printInfo('构建%s的胳膊' % self.type)

    def BuildLeg(self):
        printInfo('构建%s的大腿' % self.type)

# 瘦子
class PersonThinBuilder(PersonBuilder):
    type = '瘦子'
    def BuildHead(self):
        printInfo('构建%s的头' % self.type)

    def BuildBody(self):
        printInfo('构建%s的身体' % self.type)

    def BuildArm(self):
        printInfo('构建%s的胳膊' % self.type)

    def BuildLeg(self):
        printInfo('构建%s的大腿' % self.type)

# 指挥者
class PersonDirector():
    pb = None
    def __init__(self, pb):
        self.pb = pb

    def CreatePerson(self):
        self.pb.BuildHead()
        self.pb.BuildBody()
        self.pb.BuildArm()
        self.pb.BuildLeg()

def ClientUI():
    pb1 = PersonThinBuilder()
    pd = PersonDirector(pb1)
    pd.CreatePerson()

    pb2 = PersonFatBuilder()
    #pd2 = PersonDirector(pb2)
    pd.pb = pb2
    pd.CreatePerson()

if __name__ == '__main__':
    ClientUI()

