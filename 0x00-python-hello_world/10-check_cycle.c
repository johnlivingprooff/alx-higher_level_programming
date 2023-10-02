#include "lists.h"

/**
 * check_cycle - checks if linked list is a cycle
 * @list: the list
 * Return: 1 - if false, 0 - if true
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
