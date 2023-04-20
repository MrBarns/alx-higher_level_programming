#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to start of linked list
 *
 * Return: 1 if it is a palindrome. 0 otherwise
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *front, *back;
	unsigned int count = 0, countcpy;
	int palindromic = 0;

	if (*head == NULL)
		return (1);

	front = *head;
	for (back = front; back->next != 0; back = back->next)
	{
		if (back->next->next)
		{
			back = back->next;
			count++;
		}
		count++;
	}

	if (back->n == front->n)
		palindromic = 1;

	count++;
	while (count && palindromic)
	{
		front = front->next;
		back = front;
		count -= 2;
		for (countcpy = count; countcpy > 1; countcpy--)
			if (countcpy - 2 > 1)
			{
				back = back->next->next;
				countcpy--;
			} else
				back = back->next;

		if (front->n != back->n)
			palindromic = 0;
	}

	return (palindromic);
}
