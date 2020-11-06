#include<Python.h>//前面所做的一切配置都是为了调用这个头文件和相关库
#include<iostream>
using namespace std;
int main()
{
    Py_Initialize();//使用python之前，要调用Py_Initialize();这个函数进行初始化
    PyObject * pModule = NULL;//声明变量
    PyObject * pFunc = NULL;// 声明变量
    pModule = PyImport_ImportModule("helloworld");//这里是要调用的文件名
    pFunc= PyObject_GetAttrString(pModule, "printHello");//这里是要调用的函数名
    PyEval_CallObject(pFunc, NULL);//调用函数
    Py_Finalize();//调用Py_Finalize，这个根Py_Initialize相对应的。
    return 0;
}

