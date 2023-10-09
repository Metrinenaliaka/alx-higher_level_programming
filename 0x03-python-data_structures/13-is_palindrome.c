#include "lists.h"
/*
 * is_palidrome - checks sll if is palidrome
 * @head: pointer to head node
 * Return: 0 if not and 1 if palidrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = NULL, *fast, *slow;
	int i, count = 0;

	if ((*head)->next == NULL || *head == NULL)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}
	ptr = *head;
	for (i = 0; i < (count / 2) - 1; i++)
	{
		ptr = ptr->next;
	}
	if ((count % 2) == 0 && ptr->n != ptr->next->n)
		return (0);
	ptr = ptr->next->next;
	fast = reverse(&ptr);
	slow = fast;
	ptr = *head;
	while (fast)
	{
		if (ptr->n != fast->n)
			return (0);
		ptr = ptr->next;
		fast = fast->next;
	}
	reverse(&slow);
	return (1);
}
/**
 * reverse - function reverses node
 * @h: pointer to a head node
 * Return: pointer to head node
 */
listint_t *reverse(listint_t **h)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *ptr = *h;

	while (ptr != NULL)
	{
		next = ptr->next;
		ptr->next = prev;
		prev = ptr;
		ptr = next;
	}
	*h = prev;
	return (*h);
}
