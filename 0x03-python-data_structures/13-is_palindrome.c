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
	listint_t *slow, *fast, *prev, *temp;
	int palindromic = 1;

	fast = slow = prev = *head;
	if (*head)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev = slow;
			slow = slow->next;
		}
		if (fast != NULL)
			slow = slow->next;
		prev = 0;
		while (slow)
		{
			temp = slow->next;
			slow->next = prev;
			prev = slow;
			slow = temp;
		}
		slow = *head;
		while (prev)
		{
			if (prev->n != slow->n)
			{
				palindromic = 0;
				break;
			}
			slow = slow->next;
			prev = prev->next;
		}
	}

	return (palindromic);
}
