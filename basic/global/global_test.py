#from mytest.test_class import Test
import mytest 
#global_string = "I came from global. "

def greeting():
    print("Greeting msg: ", mytest.global_string)

if __name__ == '__main__':
    print("Enter. ")
    print(mytest.global_string)
    greeting()
    #t = Test()
    #t.run()

