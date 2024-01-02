#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * check_cycle - Entry point
 * @list: pointer
 * Return: (0)
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
