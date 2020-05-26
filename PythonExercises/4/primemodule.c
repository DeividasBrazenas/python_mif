#include <Python.h>
#include "structmember.h"


static PyObject *primeError;

static PyObject* prime_calc(PyObject *self, PyObject *args){
    int number;
    if(!PyArg_ParseTuple(args,"i", &number))
        return NULL;
        printf("Your number is %d", number);

	if(number <= 0){
		return PyErr_Format(primeError,"Wrong number error");
	}
	int i;
	for(i = 2; i <= number/2; i++){
		if(number % i == 0){
			return Py_BuildValue("i",0);
		}
	}

    return Py_BuildValue("i",1);
}

static PyMethodDef primeMethods[] = {
    {
    "prime", prime_calc, METH_VARARGS, "Check if number is prime"
    },
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef primemodule = {
    PyModuleDef_HEAD_INIT,
    "prime",
    "Module that calculates primes",
    -1,
    primeMethods
};

PyMODINIT_FUNC PyInit_prime (void){
	PyObject* module;
	module = PyModule_Create(&primemodule);
	primeError = PyErr_NewException("prime.Error",NULL,NULL);
	Py_INCREF(primeError);
	PyModule_AddObject(module,"Error",primeError);

    return module;
}