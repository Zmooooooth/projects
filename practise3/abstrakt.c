#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }
    for (int i = 0; i < 3; i++)
    {
        list[i] = i + 1;
    }
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }
    for (int y = 0; y < 3; y++)
    {
        tmp[y] = list[y];
    }
    tmp[3] = 4;
    free(list);
    for (int x = 0; x < 4; x++)
    {
        printf("%i\n",tmp[x]);
    }
    free(tmp);
    return 0;
}

