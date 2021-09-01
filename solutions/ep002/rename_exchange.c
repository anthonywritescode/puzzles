#include <Python.h>
#include <fcntl.h>
#include <sys/syscall.h>
#include <unistd.h>

/* musl libc does not define RENAME_EXCHANGE */
#ifndef RENAME_EXCHANGE
#define RENAME_EXCHANGE 2
#endif

static PyObject*
_rename_exchange(PyObject* self, PyObject* args) {
    char* path1;
    char* path2;

    if (!PyArg_ParseTuple(args, "ss", &path1, &path2)) {
        return NULL;
    }

    if (syscall(SYS_renameat2, AT_FDCWD, path1, AT_FDCWD, path2, RENAME_EXCHANGE)) {
        return PyErr_SetFromErrno(PyExc_OSError);
    } else {
        Py_RETURN_NONE;
    }
}


static struct PyMethodDef methods[] = {
    {"rename_exchange", (PyCFunction)_rename_exchange, METH_VARARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "rename_exchange",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_rename_exchange(void) {
    return PyModule_Create(&module);
};
