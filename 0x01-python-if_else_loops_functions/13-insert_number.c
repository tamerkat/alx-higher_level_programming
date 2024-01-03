#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Entry point
 * @head: pointer
 * @number: num
 * Return: (0)
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (!new)
	return (NULL);

	new->n = number;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
	new->next = node;
	return (*head = new);
	}
	while (node)
	{
	if (!node->next || node->next->n)
	{
	new->next = node->next;
	node->next = new;
	return (node);
	}
	node = node->next;
	}
	return (NULL);
}

