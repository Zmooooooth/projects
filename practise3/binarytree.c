#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
} node;

bool search(node *tree, int number);

int main(void)
{
    node *n = malloc(sizeof(node));
    n->number = 10;
    node *new = malloc(sizeof(node));
    new->number = 7;
    node *ptr = n;
    while (ptr != NULL)
    {
        if (ptr->number > n->number)
        {
            ptr = ptr->left;
        }
        else
        {
            ptr = ptr->right;
        }
    }
    free(n);
    free(new);
    return 0;


}
bool search(node *tree, int number)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        return search(tree->left, number);
    }
    else if (number > tree->number)
    {
        return search(tree->right, number);
    }
    else if (number == tree->number)
    {
        return true;
    }
    else
    {
        return false;
    }
}
