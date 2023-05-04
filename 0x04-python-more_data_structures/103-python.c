#include <Python.h>
#include <stdio.h>


/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to PyObject
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	char *str, end;
	Py_ssize_t len, ind, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	len = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n  trying string: %s\n", len, str);

	if (len < 10)
		lim = len;
	else
		lim = 10;

	printf("  first %zd bytes: ", lim);
	for (ind = 0; ind < lim; ind++)
	{
		end = ' ';
		if (ind == lim - 1)
			end = '\n';
		if (str[ind] < 0)
			printf("%02x%c", str[ind] + 256, end);
		else
			printf("%02x%c", str[ind], end);
	}
}


/**
 * print_python_list - prints some basic info about Python list objects
 * @p: pointer to PyObject
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	Py_ssize_t len, ind;

	printf("[*] Python list info\n");

	list = (PyListObject *)p;
	len = ((PyVarObject *)p)->ob_size;

	printf("[*] Size of the Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (ind = 0; ind < len; ind++)
	{
		item = list->ob_item[ind];
		printf("Element %zd: %s\n", ind, (item->ob_type)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
