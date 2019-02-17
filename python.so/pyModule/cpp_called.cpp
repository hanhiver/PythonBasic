#include "Python.h"

extern "C"
int my_add(int a, int b)
{
	return a + b;
}

extern "C"
{
static PyObject *_my_add(PyObject *self, PyObject *args)
{
	int _a, _b;
	int res; 

	if (!PyArg_ParseTuple(args, "ii", &_a, &_b))
		return NULL;

	res = my_add(_a, _b);
	return PyLong_FromLong(res);
}
}


extern "C"
{
static PyMethodDef CppModuleMethods[] =
{
	{
		"my_add", 
		_my_add, 
		METH_VARARGS,
		"My add function."
	}, 
	{NULL, NULL, 0, NULL}
};
}

extern "C"
{
PyMODINIT_FUNC initcpp_module(void)
{
	(void) Py_InitModule3("cpp_module", CppModuleMethods);
}
}



