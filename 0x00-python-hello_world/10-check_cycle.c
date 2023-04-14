#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list_t list argument
 *
 * Return: 1 if cycle is present
 * 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *curr = list;

	while (curr && curr->next && list)
	{
		list = list->next;
		curr = (curr->next)->next;

			if (curr == list)
				return (1);
	}

	return (0);
}
