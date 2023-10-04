#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head of the list
 * @number: where the insertion happens
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	/* where the list is empty or new.n is the first number on the list */
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* Travers the list to get the correct position of new.n */
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;
	return (new);
}
