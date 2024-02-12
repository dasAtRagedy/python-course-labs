#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>

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


typedef struct {
    PyObject_HEAD double a, b, c;
} TriangleObject;

double triangle_perimeter(TriangleObject *self) {
    return self->a + self->b + self->c;
}

double triangle_area(TriangleObject *self) {
    double s = triangle_perimeter(self) / 2;
    return sqrt(s * (s - self->a) * (s - self->b) * (s - self->c));
}

static PyObject* Triangle_area(TriangleObject* self) {
    double result = triangle_area(self);
    return PyFloat_FromDouble(result);
}

static PyObject* Triangle_perimeter(TriangleObject* self) {
    double result = triangle_perimeter(self);
    return PyFloat_FromDouble(result);
}

static PyMethodDef Triangle_methods[] = {
    {"area", (PyCFunction)Triangle_area, METH_NOARGS, "Calculate the area of the triangle."},
    {"perimeter", (PyCFunction)Triangle_perimeter, METH_NOARGS, "Calculate the perimeter of the triangle."},
    {NULL}
};

static int Triangle_init(TriangleObject *self, PyObject *args, PyObject *kwds) {
    if (!PyArg_ParseTuple(args, "ddd", &self->a, &self->b, &self->c)) {
        return -1; // on error
    }

    return 0;
}

static struct PyModuleDef fibonaccimodule = {
    PyModuleDef_HEAD_INIT,
    "fibonaccimodule",
    "Calculate Fibonacci number",
    -1,
    FibonacciMethods
};

static PyTypeObject TriangleType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "fibonaccimodule.Triangle", // <- this
    .tp_doc = "Triangle objects with area and perimeter methods",
    .tp_basicsize = sizeof(TriangleObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_init = (initproc)Triangle_init,
    .tp_methods = Triangle_methods,
};

PyMODINIT_FUNC PyInit_fibonaccimodule(void) {
    PyObject* m;

    if (PyType_Ready(&TriangleType) < 0)
        return NULL;

    m = PyModule_Create(&fibonaccimodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&TriangleType);
    if (PyModule_AddObject(m, "Triangle", (PyObject *)&TriangleType) < 0) {
        Py_DECREF(&TriangleType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}