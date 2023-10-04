#include "lists.h"
#include <stdlib.h>
#include <stddef.h>


/**
 * insert_node - This function inserts a number into a singly linked list
 * @head: The headnode
 * @number:The number to be inserted
 * Return: address of the new node, or NULL if it failed
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *t;

	t = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (t != NULL)
	{
		if (t->n > number)
			break;
		prev = t;
		t = t->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = t;
		if (t == *head)
			*head = new;
		else
			prev->next = new;
	}

	return (new);
}
