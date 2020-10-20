#include <stdlib.h>
#include <stdio.h> 
#include <iostream> 
#include <string> 

extern "C"
{

void hello()
{
    printf("Hello! \n");
}

void hello_cpp()
{
    std::cout << "Hello_cpp! " << std::endl;
}

void hello_string()
{
    std::string hello = "Hello, string! ";
    std::cout << hello << std::endl; 
}

void hello_to(const char* name)
{
    printf("Hello %s. \n", name);
}

void hello_to2(const char* name)
{
    std::string n(name);
    std::cout << "Hello " << n << std::endl; 
}

void hello_string_int(const char* name, unsigned int m)
{
    for (int i=0; i<m; ++i)
    {
        std::cout << "OK, " << name << std::endl;
    }
}
} // extern "C"