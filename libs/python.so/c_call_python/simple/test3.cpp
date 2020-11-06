#include <iostream>
#include <string> 

#include <Python.h>

int main(int argc, char* argv[])
{
    PyObject *pName, *pModule, *pFunc;
    PyObject *pArgs, *pValue;

    // Initialize the python env. 
    Py_Initialize();

    // Run python code directly to include the current folder to path. 
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");
    PyRun_SimpleString("print(sys.path)");

    pName = PyUnicode_DecodeFSDefault("class_A_test");

    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (NULL != pModule)
    {
        pFunc = PyObject_GetAttrString(pModule, "run2_wrapper");

        pArgs = PyTuple_New(1);
        pValue = PyLong_FromLong(5L);
        PyTuple_SetItem(pArgs, 0, pValue);

        if (!pValue)
        {
            Py_DECREF(pArgs);
            Py_DECREF(pModule);
            std::cout << "Cannot convert argument" << std::endl;
            return 1;
        }

        if (pFunc && PyCallable_Check(pFunc))
        {
            pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);
            if (NULL != pValue)
            {
                std::cout << "Result of the call: " << PyLong_AsLong(pValue) << std::endl;
                Py_DECREF(pValue);
            }
            else
            {
                Py_DECREF(pFunc);
                Py_DECREF(pModule);
                PyErr_Print();
                std::cout << "Call failed. " << std::endl; 
                return 1;
            }
        }
        else
        {
            if (PyErr_Occurred())
            {
                PyErr_Print();
            }
            std::cout << "Cannot find function." << std::endl; 
        }
        
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }
    else
    {
        std::cout << "Failed to load module. " << std::endl; 
    }

    if (Py_FinalizeEx() < 0)
    {
        return -1;
    }
    
    return 0;
}