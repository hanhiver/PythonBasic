#include <stdio.h>

int testlib()
{
    printf("Test OK, inside lib.\n");
    return 0;
}

int func_add(int a, int b)
{
    return a + b;
}

int func_mul(int a, int b)
{
    return a * b;
}

int call_func( int (*func)(int, int) )
{
    int a = 2, b = 3;
    int c = (*func)(a, b);
    printf("Result = %d.\n", c);
}

int main()
{
    int (*func)(int, int);
    
    testlib();

    printf("Test func_add: ");
    func = func_add;
    call_func(func);
    
    printf("Test func_mul: ");
    func = func_mul;
    call_func(func);

    return 0;
}


