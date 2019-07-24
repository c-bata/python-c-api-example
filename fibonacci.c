#include <Python.h>


long long fibonacci(unsigned int n) {
    if (n < 2) {
        return 1;
    } else {
        return fibonacci(n-2) + fibonacci(n-1);
    }
}


static PyObject* fibonacci_py(PyObject* self, PyObject *args, PyObject *keywds) {
    long n;
    int nogil = 0;
    long long fib;
    PyObject *result = NULL;
    static char *kwlist[] = {"n", "nogil", NULL};

    if (PyArg_ParseTupleAndKeywords(args, keywds, "l|p", kwlist, &n, &nogil)) {
        if (n < 0) {
            PyErr_SetString(PyExc_ValueError, "n must not be less than 0");
        } else if (nogil == 1) {
            Py_BEGIN_ALLOW_THREADS;
            fib = fibonacci((unsigned int)n);
            Py_END_ALLOW_THREADS;
            result = Py_BuildValue("L", fib);
        } else {
            fib = fibonacci((unsigned int)n);
            result = Py_BuildValue("L", fib);
        }
    }

    return result;
}


static char fibonacci_docs[] =
    "fibonacci(n): Return nth Fibonacci sequence number "
    "computed recursively\n";

static PyMethodDef fibonacci_module_methods[] = {
    {"fibonacci", (PyCFunctionWithKeywords)fibonacci_py,
     METH_VARARGS | METH_KEYWORDS,
     fibonacci_docs},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fibonacci_module_definition = {
    PyModuleDef_HEAD_INIT,
    "fibonacci",
    "Extension module that provides fibonacci sequence function",
    -1,
    fibonacci_module_methods
};

PyMODINIT_FUNC PyInit_fibonacci(void) {
    Py_Initialize();

    return PyModule_Create(&fibonacci_module_definition);
}