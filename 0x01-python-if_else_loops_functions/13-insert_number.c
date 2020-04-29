#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *@head: list to insert number into
 *@number: number to insert
 *
 * Return: address of the new node, or Null if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	if (head == NULL)
		return (NULL);

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (current->next == NULL)
	{
		if (current->n > number)
		{
			new->next = current;
			head = &new;
			return (new);
		}
		else
		{
			current->next = new;
			new->next = NULL;
			return (new);
		}

	}
	while (current->next != NULL
	       && current->n < number
	       && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
