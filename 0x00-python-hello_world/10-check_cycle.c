#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to the head node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prev, *fast;

	prev = fast = list;

	while (prev && fast && fast->next)
	{
		prev = prev->next;
		fast = fast->next->next;
		if (prev == fast)
			return (1);
	}
	return (0);
}
