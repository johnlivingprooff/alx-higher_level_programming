#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the list
 * Return: 0 if not palindrome, 1 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev = NULL, *nex = NULL;
	listint_t *firstHalf, *secondHalf;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* empty list is palindrome */

	slow = *head;
	fast = *head;
	/* finding the middle of l-list */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/* Reverse the second half of l-list */
	while (slow != NULL)
	{
		nex = slow->next;
		slow->next = prev;
		prev = slow;
		slow = nex;
	}
		firstHalf = *head;
		secondHalf = prev;
	/* Comparing the first& second halves */
	while (secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
			return (0); /* not a palindrome list */
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}

	return (1); /* a palindrome list */
}
