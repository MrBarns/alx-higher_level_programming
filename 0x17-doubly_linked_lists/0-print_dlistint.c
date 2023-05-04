#include "lists.h"

/**
 * print_dlistint - prints all elements of a dlistint_t list
 * @h: pointer to list header
 *
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t size = 0;

	for (; h; h = h->next)
	{
		printf("%d\n", h->n);
		size++;
	}

	return (size);
}
