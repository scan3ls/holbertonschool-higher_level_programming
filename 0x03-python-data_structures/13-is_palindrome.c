#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a list is a palindrome
 *@head: list to check
 *
 * Return: 0 if False, 1 if True
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i1, i2, length;
	int tmpArray[1024*5];

	if (*head == NULL)
		return (1);

	temp = *head;

	for (length = 0; temp != NULL; length++)
	{
		tmpArray[length] = temp->n;
		temp = temp->next;
	}

	i1 = (length % 2 == 0) ? (length / 2) - 1 : (length / 2);
	i2 = (length % 2 == 0) ? i1 + 1 : i1;

	while (tmpArray[i1] == tmpArray[i2])
	{
		i1--;
		i2++;
		if (i1 < 0 || i2 > length)
			return (1);
	}
	return (0);

}
