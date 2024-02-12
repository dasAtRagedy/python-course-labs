#define PY_SSIZE_T_CLEAN
#include <Python.h>

unsigned long long fibonacci(int n) {
    if (n < 2) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

static PyObject* py_fibonacci(PyObject* self, PyObject* args) {
    int n;

    if (!PyArg_ParseTuple(args, "i", &n)) {
        PyErr_SetString(PyExc_TypeError, "n must be an integer");
        return NULL;
    }

    if (n < 0) {
        PyErr_SetString(PyExc_IndexError, "Index is out of range");
        return NULL;
    }

    unsigned long long answer = fibonacci(n);

    return PyLong_FromUnsignedLongLong(answer);
}

static PyMethodDef FibonacciMethods[] = {
    {"fibonacci", py_fibonacci, METH_VARARGS, "Calculate Fibonacci number"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibonaccimodule = {
    PyModuleDef_HEAD_INIT,
    "fibonaccimodule",
    "Calculate Fibonacci number",
    -1,
    FibonacciMethods
};

PyMODINIT_FUNC PyInit_fibonaccimodule(void) {
    return PyModule_Create(&fibonaccimodule);
}