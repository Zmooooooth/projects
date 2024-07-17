#include <stdio.h>
#include <stdlib.h>

typedef struct node
    {
        int number;
        struct node *next;
    } node;

int main(int argc, char *argv[])
{
    node *list = NULL;
    for (int i = 0; i < argc; i++)
    {
        int number = atoi(argv[i]);
        //printf("%i\n",number);
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Could not assign pointer\n");
            return 1;
        }
        n->number = number;
        n->next = list;
        list = n;
    }
    node *ptr = list;
    while (ptr != NULL)
    {
        printf("Node: %i\n",ptr->number);
        ptr = ptr->next;
    }
    printf("Done!\n");
}
