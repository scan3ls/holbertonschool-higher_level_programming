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
	while (current != NULL && current->n < number && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	new->n = number;

	return (new);
}
