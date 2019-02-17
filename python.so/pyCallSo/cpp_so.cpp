#include <iostream>

extern "C"

int my_add(int a, int b)
{
	std::cout<<"The result is: "<<a+b<<std::endl;
	return a + b;
}


