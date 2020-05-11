#include <iostream>

extern "C"
{

void testlib()
{
    std::cout<<"Lib load OK."<<std::endl;
}

class cppClass
{
    public:
        cppClass();
        cppClass(int input);
        ~cppClass();
        int callme();

    private:
        int _value;
};

cppClass::cppClass()
{
    _value = 0;
    std::cout<<"cppClass created."<<std::endl;
}

cppClass::cppClass(int input)
{
    _value = input; 
    std::cout<<"cppClass created."<<std::endl;
}

cppClass::~cppClass()
{
    std::cout<<"cppClass deleted."<<std::endl;
}

int cppClass::callme()
{
    std::cout<<"Value: "<<_value<<std::endl;
    _value ++;
    return _value;
}


cppClass *mycc;
int test_value = 0; 
int *test_pointer = new int;

void init_class()
{
    mycc = new cppClass(3);
}

void call_class()
{
    mycc->callme();
}

void delete_class()
{
    delete mycc;
}


void check_value()
{
    std::cout<<"Value: "<<test_value<<std::endl;
    test_value ++;
}

void init_pointer()
{
    *test_pointer = 1;
}

void check_pointer()
{
    std::cout<<"Pointer: "<<*test_pointer<<std::endl;
    *test_pointer = *test_pointer + 1;
    //std::cout<<"Pointer: "<<*test_pointer<<std::endl;
}

} // extern "C"


int main()
{

    init_class();
    
    call_class();
    call_class();

    delete_class();

    
/*
    cppClass mycc = new cppClass;

    init(&mycc);
    call(mycc);
    call(mycc);
*/
    return 0;
}




