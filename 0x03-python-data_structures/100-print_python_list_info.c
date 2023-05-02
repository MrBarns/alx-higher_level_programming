#include <Python.h>
#include <stdio.h>


/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	Py_ssize_t size, ind;

	size = Py_SIZE(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (ind = 0; ind < size && size > 0; ind++)
	{
		item = PyList_GetItem(p, ind);
		printf("Element %zd: %s\n", ind, Py_TYPE(item)->tp_name);
	}
}
