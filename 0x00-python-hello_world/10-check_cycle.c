#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a singly linked list has a cycle
 *@list: list to check
 *
 * Return: 0 if has No Cycle, 1 if has Cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	int length, i, size = 0;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list;
	while (fast > fast->next && fast->next != NULL)
	{
		fast = fast->next;
		size++;
	}
	fast = list;
	for (i = 0; i < size; i++)
	{
		if (slow->n == fast->n)
		{
			fast = slow->next;
			for (length = 1; fast->n == slow->n; length++)
				fast = fast->next;
			for (; length > 0; length--)
			{
				if (fast->n != slow->n)
					break;
				if (fast->next == NULL)
					return (0);
				fast = fast->next;
				slow = slow->next;
				if (length == 1)
					return (1);
			}
			fast = slow->next;
		}
		else
		{
			if (next_nodes(slow, fast))
				return (0);
		}
	}
	return (0);
}

/**
 * next_nodes - moved node1 forward by one and node2 by 2
 *@node1: slow node
 *@node2: fast node
 *
 * Return: 1 on success, 0 on failure
 */

int next_nodes(listint_t *node1, listint_t *node2)
{
	if (node1->next == NULL)
		return (0);
	node1 = node1->next;

	if (node2->next == NULL)
		return (0);
	node2 = node2->next;
	if (node2->next == NULL)
		return (0);
	node2 = node2->next;

	return (1);
}
