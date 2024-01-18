#include "lists.h"

/**
 * print_dlistint - Entry point
 * @h: pointer
 * Return: always (0)
*/

size_t print_dlistint(const dlistint_t *h)
{
	size_t i;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		i++;
	}
	return (i);
}
