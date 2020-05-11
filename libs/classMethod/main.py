from classA import A 
import addMethod2A


def useA(a):
	a.printName()
	a.printArgs()
	a.printAge("LALALA")

if __name__ == '__main__':
	#a = A("Original")
	a = addMethod2A.getA(a=1, b=2, c="Test")
	useA(a)

