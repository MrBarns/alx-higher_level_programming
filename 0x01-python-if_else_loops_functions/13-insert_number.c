#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to pointer to head of list
 * @number: number to be added
 *
 * Return: pointer to new node if successful
 * NULL otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = 0, *curr, *new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		free(new);
		return (0);
	}
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if ((*head)->next == NULL)
	{
		if ((*head)->n >= number)
		{
			new->next = *head;
			*head = new;
		} else
		{
			(*head)->next = new;
			new->next = 0;
		}
		return (new);
	}
	for (curr = *head; curr != NULL; prev = curr, curr = curr->next)
	{
		if (curr->n >= number)
		{
			if (!prev)
				new->next = curr, *head = new;
			else
				prev->next = new, new->next = curr;
			return (new);
		}
	}
	prev->next = new;
	new->next = 0;
	return (new);
}
