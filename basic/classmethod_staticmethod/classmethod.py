# classmethod将函数变成类方法。
# 调用的时候cls会自动指向self
class sample:
    language = "C++"
    def __init__(self):
        self.language = "python"

    @classmethod
    def get_class_attr(cls):
        return cls.language

if __name__ == "__main__":
    print("sample.language:", sample.language)
    r = sample.get_class_attr()
    print("get class attribute:", r)
    f = sample()
    print("instance attribute:", f.language)
    print("instance get_class_str:", f.get_class_attr())