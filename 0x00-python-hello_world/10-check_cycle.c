#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 *@list: list to check
 *
 * Return: 0 if has No Cycle, 1 if has Cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);
	temp = list;

	while (temp != NULL)
	{
		if (temp->next > temp)
			return (1);
		temp = temp->next;
	}

	return (0);
}
